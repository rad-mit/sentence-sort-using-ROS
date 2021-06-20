#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from msgs.msg import string_array

# Topic callback function.
def CallbackFn(data):
    words=data.data.split()
    words.sort()
    simple_publisher1 = rospy.Publisher('topic_2', string_array, queue_size = 10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
    	simple_publisher1.publish(words)
        rate.sleep()

def stringListener():
    rospy.init_node('sort_node' , anonymous = False)
    rospy.Subscriber('topic_1' , String, CallbackFn)
    simple_publisher1 = rospy.Publisher('topic_2', string_array, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    stringListener()
