import os

from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Your TurtleBot model (e.g., 'burger' or 'waffle')
    turtlebot_model = 'burger'

    # Number of TurtleBots to spawn
    num_turtlebots = 20

    # Spacing between TurtleBots along the x-axis
    spacing_x = 1.0

    # Launch file directory
    launch_file_dir = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'
    )

    # Include the Gazebo empty world launch
    empty_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(launch_file_dir, 'empty_world.launch.py')
        ])
    )

    # Create nodes to spawn multiple TurtleBots
    spawn_turtlebots = [
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=[
                '-entity', f'turtlebot{i}',
                '-file', f'/opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdfgit ,
                '-x', str(i * spacing_x),  # Adjust the x pose
                '-y', '0.0',  # Adjust the y pose
                '-z', '0.01'
            ],
        ) for i in range(1, num_turtlebots + 1)
    ]

    return LaunchDescription([
        empty_world_launch,
        *spawn_turtlebots
    ])
