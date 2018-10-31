# Turtlesim Set Pose Challenge!!

This package is used to send the turtle from turtlesim to an specific goal!

## Requirements
  * [Ubuntu 16.04 LTS (Xenial)](http://releases.ubuntu.com/14.04/) 
  * [ROS Kinetic Kame](http://wiki.ros.org/indigo/Installation/Ubuntu) 
  * [ROS Workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
  * [Turtlesim](http://wiki.ros.org/turtlesim)

## Features
* Turtlesim challenge Launch - Launch the turtlesim together with roscore and the set pose script:
```
$ roslaunch turtlesim_challenge turtlesim_challenge.launch
```
* Set Pose node - Sends the turtle to an specific goal using the user input.

    After lauching the turtlesim node
```
$ rosrun turtlesim_challenge set_goal.py
```
## Installation

Clone the repository

```
$ git clone https://github.com/clebercoutof/turtle_challenge
```

Go to the root of your catkin workspace and do a catkin_make:
```
$ catkin_make
```


### Prerequisites
The turtlesim already comes with the ros installation, but if you can't find it in your system run:
```
$ sudo apt-get install ros-kinetic-turtlesim
```

## Built With
* [Visual Studio Code](https://code.visualstudio.com/) - The coding IDE


## Authors

* **Cleber Couto Filho** - *Initial work* - [clebercoutof](https://github.com/clebercoutof)

## Acknowledgments
Thanks to everyone of the Robotics Team who motivated me with the work.

