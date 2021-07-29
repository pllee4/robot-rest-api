# Robot REST API

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

## Running of program

- Go to your catkin_workspace, eg catkin_ws/src

```
$ git clone https://github.com/pllee4/robot-rest-api.git
$ cd ..
$ catkin_make
$ roslaunch robot-rest-api rest_server.launch ## for server
$ roslaunch robot-rest-api rest_client.launch ## for client
```

## References
- [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/)