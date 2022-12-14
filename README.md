# nav2_playground
A robot test environment using foxy and navigation2 in docker.

# models used 
/workspaces/nav2_playground_zxx/src/aws-robomaker-small-warehouse-world/models 

/opt/ros/foxy/share/turtlebot3_gazebo/models

 ./models 

# usage

1:  git clone 

2: open folder in vscode

3:  reopen in container

4:  build container

5: in vscode, Terminal -> Run Task -> install denpendencies

6: in vscode, Terminal -> Run Task -> Build

7: source ./install/setup.bash

8: ros2 launch nav2_simple_commander waypoint_follower_example_launch.py 

# note
if during building, an error occured like this "c++: fatal error: Killed signal terminated program cc1plus', just build again.



