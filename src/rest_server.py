#!/usr/bin/env python
"""
rest_server.py
Created on: Jul 31, 2021 18:03
Description: REST API Server
Copyright (c) 2021 Pin Loon Lee (pllee4)
"""
# ROS
import argparse
import rospy
from actionlib_msgs.msg import GoalStatusArray

# Flask
from flask import Flask
from flask_restful import Resource, Api

robot_data = {}
robot_data["data_arrived"] = False


def move_base_status_callback(data):
    """callback from ROS topic /move_base/status"""
    if data.status_list:
        robot_data["status"] = data.status_list[0].status
        robot_data["text"] = data.status_list[0].text
        robot_data["data_arrived"] = True


class MoveBaseStatus(Resource):
    """queried by /api/robot/status"""
    @staticmethod
    def get():
        """client request or curl"""
        if robot_data["data_arrived"]:
            robot_data["data_arrived"] = False
            response = {
                "status": robot_data["status"],
                "text": robot_data["text"],
            }, 200
        else:
            response = {"message": "Invalid status value"}, 400
        return response


# ROS
rospy.init_node("ros_rest_server", disable_signals=True)
rospy.Subscriber(
    "/move_base/status", GoalStatusArray, move_base_status_callback
)

# Flask
app = Flask("REST Server")
api = Api(app)
api.add_resource(MoveBaseStatus, "/api/robot/status")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="REST Server")
    parser.add_argument(
        "port_number", nargs="?", default="7201", type=int, help="port number"
    )
    parser.add_argument(
        "ip_address",
        nargs="?",
        default="127.0.0.1",
        help="ip_address for server",
    )
    margs = parser.parse_args(rospy.myargv()[1:])
    port_number = margs.port_number
    ip_address = margs.ip_address
    app.run(ip_address, port=port_number)
