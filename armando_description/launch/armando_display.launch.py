from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    
    arm_description_path = os.path.join(get_package_share_directory('armando_description'))
    
    
    urdf_path = os.path.join(arm_description_path, "urdf", "armando.urdf.xacro")
    
    
    rviz_config = os.path.join(arm_description_path, "config", "config.rviz")

    # Read the URDF file
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    robot_description = {"robot_description": robot_desc}
    
    # Node robot_state_publisher
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description]
    )
    
    # Node joint_state_publisher
    joint_state_publisher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        output="screen"
    )
    
    # Node rviz2 con configurazione rviz 
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config] 
    )
    
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])
