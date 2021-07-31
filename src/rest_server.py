#!/usr/bin/env python
# ROS
import rospy
import threading
from actionlib_msgs.msg import GoalStatusArray

# Flask
from flask import Flask
from flask_restful import Resource, Api

# Python
import argparse

# ROS
status = 0
text = ""
new_data_arrived = False


def move_base_status_callback(data):
    # TODO: update data and pass to server
    if (data.status_list):
        global status
        global text
        global new_data_arrived
        status = data.status_list[0].status
        text = data.status_list[0].text
        new_data_arrived = True


def ros_node():
    rospy.init_node('ros_rest_server', disable_signals=True)
    rospy.Subscriber("/move_base/status", GoalStatusArray,
                     move_base_status_callback)


threading.Thread(target=ros_node).start()

# Flask
app = Flask("REST Server")
api = Api(app)


class MoveBaseStatus(Resource):
    def get(self):
        # TODO: get data from robot_node
        # TODO: check whether there is topic
        global new_data_arrived
        if (new_data_arrived):
            new_data_arrived = False
            return {'status': status, 'text': text}, 200
        else:
            return {'message': "Invalid status value"}, 400


api.add_resource(MoveBaseStatus, "/api/robot/status")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="REST Server")
    parser.add_argument(
        "port_number", nargs="?", default="7201", type=int, help="port number"
    )
    parser.add_argument(
        "ip_address", nargs="?", default="127.0.0.1", help="ip_address for server"
    )
    margs = parser.parse_args(rospy.myargv()[1:])
    port_number = margs.port_number
    ip_address = margs.ip_address
    app.run(ip_address, port=port_number)
