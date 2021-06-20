# Sort the words of a sentence using ROS
## Description
This project uses three custom ROS nodes to sort all the words of any given sentence. 
The first node, namely **/input_node** accepts the sentence as string input from the terminal and passes it to the second node via **/topic_1**. The second node called the **/sort_node** splits the sentence into words, stores them in a list and then sorts the list. It then passes the list to the third node via **/topic_2**. To pass a list, a custom ROS message type called **string_array** is used. It can be found in **/src/msgs/msg/string_array.msg**. 

## Instructions
To work with this, you need to have ROS kinetic/
