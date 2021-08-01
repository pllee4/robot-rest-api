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

## Debugging

- If there is failure of running the above commands, 
  you can verify the environment using [Docker](https://docs.docker.com/engine/install/ubuntu/)
- After install Docker, run the following commands

```
$ sudo docker pull ros:melodic
$ sudo docker run -it --name debug ros:melodic
$ apt-get update
$ apt install wget
$ wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
$ python2.7 get-pip.py
$ mkdir /catkin_ws/src -p && cd /catkin_ws/src
$ git clone https://github.com/pllee4/robot-rest-api && cd robot-rest-api
$ pip install -r requirements.txt
$ cd /catkin_ws && catkin_make
$ source devel/setup.bash
$ roslaunch robot-rest-api rest_server.launch ## for server
$ python /catkin_ws/src/robot-rest-api/src/rest_client.py ## for client
```

## References
- [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/)