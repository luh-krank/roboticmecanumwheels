cmake_minimum_required(VERSION 3.0.2)
project(mecanum_bot)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  tf
  nav_msgs
  sensor_msgs
  move_base
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

catkin_install_python(PROGRAMS
  scripts/mecanum_cmd_serial.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
