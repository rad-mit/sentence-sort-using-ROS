#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def simplePublisher():
    simple_publisher = rospy.Publisher('topic_1', String, queue_size = 10)
    rospy.init_node('input_node_pub', anonymous = False)
    rate = rospy.Rate(10)
    
    # The string to be published on the topic
    topic1_content = raw_input('Enter the sentence to be sorted: \n')
    
    while not rospy.is_shutdown():
    	simple_publisher.publish(topic1_content)
        rate.sleep()
        
if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
