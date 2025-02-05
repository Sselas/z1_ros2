# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration
# from ament_index_python.packages import get_package_share_directory


# def generate_launch_description():
#     # Déclaration des arguments de lancement
#     declared_arguments = [
#         DeclareLaunchArgument(
#             'use_sim_time', 
#             default_value='true', 
#             description='Utiliser le temps simulé'
#         ),
#         DeclareLaunchArgument(
#             'rviz_config', 
#             default_value='config/moveit.rviz', 
#             description='Fichier de configuration RViz'
#         ),
#     ]

#     # Configuration des chemins
#     moveit_config_path = get_package_share_directory('z1_moveit_config')
#     rviz_config_path = LaunchConfiguration('rviz_config')

#     # Inclure le fichier de lancement move_group
#     move_group_launch = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             moveit_config_path + '/launch/move_group.launch.py'
#         ),
#         launch_arguments={
#             'use_sim_time': LaunchConfiguration('use_sim_time')
#         }.items()
#     )

#     # Inclure le fichier de lancement RViz
#     rviz_launch = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             moveit_config_path + '/launch/moveit_rviz.launch.py'
#         ),
#         launch_arguments={
#             'rviz_config': rviz_config_path,
#             'use_sim_time': LaunchConfiguration('use_sim_time')
#         }.items()
#     )

#     return LaunchDescription(declared_arguments + [move_group_launch, rviz_launch])


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os


def generate_launch_description():
    # Déclaration des arguments
    declared_arguments = [
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="Use simulation time if true"
        ),
    ]

    use_sim_time = LaunchConfiguration("use_sim_time")
    if use_sim_time:
        print(f"*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********\nUSING SIM TIME : {use_sim_time}\n**********\n*********\n********\n*******\n******\n*****\n****\n***\n**\n*")


    # Chemins des fichiers de configuration
    pkg_share = os.path.join(os.getenv('COLCON_PREFIX_PATH'), 'z1_moveit_config', 'share', 'z1_moveit_config')

    # Lancer le fichier move_group.launch.py
    move_group_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'move_group.launch.py')
        ),
        launch_arguments={"use_sim_time": use_sim_time}.items()
    )

    # Lancer RViz avec la configuration MoveIt!
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_share, 'config', 'moveit.rviz')],
        parameters=[{"use_sim_time": use_sim_time}]
    )

    return LaunchDescription(declared_arguments + [move_group_launch, rviz_node])
