#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    rospy.init_node("test_node")

    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()
        
