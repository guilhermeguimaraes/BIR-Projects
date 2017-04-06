#!/usr/bin/env python 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class roboturtle():

  def __init__(self):
     
     rospy.init_node('roboturtle_setpoint', anonymous = True)
     self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

     self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
     self.pose = Pose()
     self.rate = rospy.Rate(10)

  def callback(self, data):
    
     self.pose = data
     self.pose.x = round(self.pose.x, 4)
     self.pose.y = round(self.pose.y, 4)



  def movetopoint(self):
     
     final_pose = Pose()
     final_pose.x = input("Enter the desired x coordinate: ")
     final_pose.y = input("Enter the desired y coordinate: ")
     tolerance = input("Enter desired tolerance: ")
     vel_msg = Twist()
     
     while sqrt(pow((final_pose.x - self.pose.x), 2) + pow((final_pose.y - self.pose.y), 2)) >= tolerance:

               vel_msg.linear.x = 3.0 * sqrt(pow((final_pose.x - self.pose.x), 2) + pow((final_pose.y - self.pose.y), 2))
               vel_msg.linear.y = 0
               vel_msg.linear.z = 0
   
               vel_msg.angular.x = 0
               vel_msg.angular.y = 0
               vel_msg.angular.z = 8 * (atan2(final_pose.y - self.pose.y, final_pose.x - self.pose.x) - self.pose.theta)

               self.velocity_publisher.publish(vel_msg)
               self.rate.sleep()
               
     vel_msg.linear.x = 0
     vel_msg.angular.z =0
     self.velocity_publisher.publish(vel_msg)
               
     rospy.spin()
               
if __name__ == '__main__':
     try:
        x = roboturtle()
        x.movetopoint()
     except rospy.ROSInterruptException: pass
 
  
     
     
