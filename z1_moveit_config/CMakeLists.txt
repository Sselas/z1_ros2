cmake_minimum_required(VERSION 3.22)
project(z1_moveit_config)

find_package(ament_cmake REQUIRED)

ament_package()

find_package(moveit_ros_planning_interface REQUIRED)
find_package(z1_description REQUIRED)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})
