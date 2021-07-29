#!/usr/bin/env python
# ROS
import rospy
import threading
from actionlib_msgs.msg import GoalStatusArray

# Flask
from flask import Flask
from flask_restful import Resource, Api

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
    rospy.spin()


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
            return {'status': status, 'text': text}, 200
            new_data_arrived = False
        else:
            return {'message': "Invalid status value"}, 400


api.add_resource(MoveBaseStatus, "/api/robot/status")

if __name__ == '__main__':
    app.run(port=7201)
