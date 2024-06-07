import os
from  ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    rm_63_gazebo_up = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory(('rm_gazebo')),'launch', 'gazebo_63_demo.launch.py'))
    )

    rm_63_gazebo_moveit = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory(('rm_63_config')),'launch', 'gazebo_moveit_demo.launch.py'))
    )

    return LaunchDescription([
    rm_63_gazebo_up,
    rm_63_gazebo_moveit
    ])