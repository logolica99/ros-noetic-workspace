#!/usr/bin/env  python3

import rospy
from sensor_msgs.msg import Range


def range_callback(msg):
    rospy.loginfo(msg.range)


if __name__ == "__main__":
    rospy.init_node("sonar_subscriber")

    sub = rospy.Subscriber("/ultrasound", Range, callback=range_callback)

    rospy.loginfo("node has been started")

    rospy.spin()  # keeps the code running
