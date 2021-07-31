# Robot REST API
![GitHub Workflow Status](https://github.com/pllee4/robot-rest-api/workflows/ROS/badge.svg)
![GitHub Workflow Status](https://github.com/pllee4/robot-rest-api/workflows/ROS%20Pylint/badge.svg)
![GitHub Workflow Status](https://github.com/pllee4/robot-rest-api/workflows/Pylint/badge.svg)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/pllee4/robot-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pllee4/robot-rest-api/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/pllee4/robot-rest-api/badge)](https://www.codefactor.io/repository/github/pllee4/robot-rest-api/overview/)

## Desription
- This repo provides REST API for client to get the robot status that is reflected from ROS topic /move_base/status.

## Rostopic

- To get rostopic of /move_base/status, please refer to the reference for installation of turtlebot3 package.
- If you are at ROS network where there is available /move_base/status topic being published, you can skip this step.

```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch 
```

## Running of server

- Go to your catkin_workspace, eg catkin_ws/src

```
$ git clone https://github.com/pllee4/robot-rest-api.git
$ cd ..
$ catkin_make
$ roslaunch robot-rest-api rest_server.launch
```

## Running of client

```
$ git clone https://github.com/pllee4/robot-rest-api.git
$ cd robot-rest-api
$ python src/rest_client.py
```

## References
- [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/)