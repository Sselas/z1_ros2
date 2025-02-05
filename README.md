# Unitree Z1 ROS2 package

This is a community-driven package that enable the [Z1 Manipulator](https://shop.unitree.com/products/unitree-z1) from [Unitree](https://www.unitree.com/) to work in ROS2.

[![Humble CI](https://github.com/idra-lab/z1_ros2/actions/workflows/humble.yml/badge.svg)](https://github.com/idra-lab/z1_ros2/actions/workflows/humble.yml)
[![Jazzy CI](https://github.com/idra-lab/z1_ros2/actions/workflows/jazzy.yml/badge.svg)](https://github.com/idra-lab/z1_ros2/actions/workflows/jazzy.yml) 
[![Rolling CI](https://github.com/idra-lab/z1_ros2/actions/workflows/rolling.yml/badge.svg)](https://github.com/idra-lab/z1_ros2/actions/workflows/rolling.yml)

## Installation

To use this package in ROS2, first clone this repository in a ROS2 workspace, e.g.:
``` bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/idra-lab/z1_ros2.git
```

Then, it is simply necessary to build the workspace:
``` bash
cd ~/ros2_ws
colcon build
```


## ROS2 packages

This repository contains different sub-packages:

- `z1_description`: contains the URDFs for the Z1 robot, as well as its meshes;
- `z1_bringup`: contains configuration and launch files for the Z1 manipulator;
- `z1_hardware_interface`🚧⚠️ **work in progress**⚠️🚧: provides the [ROS2 control](https://control.ros.org/rolling/index.html) hardware interface for the Z1 manipulator.

## Testing the robot

To test the robot in the simulation environment, you can directly call the command
```
ros2 launch z1_bringup z1.launch.py
```
More details on how to launch the robots can be found in the `z1_bringup` package [README](z1_bringup/README.md).

## Testing the robot

Launching the RViz and MoveIt! simulation is achieved with with the command :
```
ros2 launch z1_moveit_config custom.launch.py
```

## Forcing sim_time

```
ros2 param set /move_group use_sim_time true
```


## Contributing

Everyone is welcome to contribute to this repository. 

If you want to improve something, or have some particular request, please first open an issue to disclose your idea with everyone.

As general rule, please develop your feature/bug-fix on a new branch, and create a pull request targeting the **development branch** (`devel`).
There we will make sure that the change is working as expected, and will update the reference of the `main` branch accordingly, to guarantee the stability of such branch.
