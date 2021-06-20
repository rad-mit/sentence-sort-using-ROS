# Sort the words of a sentence using ROS
## Description
This project uses three custom ROS nodes to sort all the words of any given sentence.   

The first node, namely `/input_node` accepts the sentence as string input from the terminal and passes it to the second node via `/topic_1`. The second node called the `/sort_node` splits the sentence into words, stores them in a list and then sorts the list. It then passes the list to the third node via `/topic_2`. To pass a list, a custom ROS message type called `string_array` is used. It can be found in `/src/msgs/msg/string_array.msg`. The third node is `/output_node` and simply joins the words in the sorted list and prints the sentence onto the terminal. 

## Instructions
To work with this, you need to have `Ubuntu 16.04 + ROS Kinetic` or `Ubuntu 18.04 + ROS Melodic` installed locally or in a virtual machine.  

1.Open a new terminal window using `Ctrl+Alt+T`.  
2. Clone this repository  
`$ git clone https://github.com/rad-mit/sentence-sort-using-ROS`  
3.Rename the folder to whatever you want to call your new ROS workspace, say `catkin_ws`  
`$ mv sentence-sort-using-ROS catkin_ws`  
4.Change the current working directory to `catkin_ws`  
`$ cd catkin_ws`  
5. Build your workspace using 
`$ catkin_make`  
6. Source your `setup.bash` file  
`$ source devel/setup.bash`  
7. Launch the `sort.launch` file from the ROS package called `task`  
`$ roslaunch task sort.launch`  
8. If successful, a prompt to enter the required sentence will appear on the terminal. Type in the senetence you want to be sorted and press `Enter`.  
9. The sorted sentence will be printed onto the terminal continuously till you terminate the process using `Ctrl+C`.  
