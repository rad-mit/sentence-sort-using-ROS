#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from msgs.msg import string_array

# Topic callback function.
def CallbackFn(data):
	res=" ".join(data.result)
	rospy.loginfo('%s', res)

def stringListener():
    rospy.init_node('output_node' , anonymous = False)
    
    rospy.Subscriber('topic_2' , string_array, CallbackFn)

    rospy.spin()

if __name__ == '__main__':
    stringListener()
