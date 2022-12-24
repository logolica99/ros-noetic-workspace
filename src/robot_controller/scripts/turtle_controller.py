#!/usr/bin/env  python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def pose_callback(pose: Pose):
    cmd = Twist()
    rospy.loginfo(pose)
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    cmd_vel_publisher_.publish(cmd)


if __name__ == "__main__":
    rospy.init_node("turtle_controller")

    cmd_vel_publisher_ = rospy.Publisher("/turtle1/cmd_vel", Twist, 10)
    pose_subscriber_ = rospy.Subscriber(
        "/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Turtle controller has been started")

    rospy.spin()
