#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtleChallenge():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtle_challenge_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(5)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self,x,y,distance_tolerance):
        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y
        vel_msg = Twist()

        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        print('The turtle moved!\n')

    def turtle_wait_for_goal(self):
        print('Welcome to the turtlesim go to goal challenge! \n')
        while not rospy.is_shutdown():
            #Checks if the user wants to send one goal
            print('Press Enter to Continue or any key to quit')
            a = raw_input()
            if len(a) == 0:
                #Receive the coordinates
                x = input("Set your x goal:")
                y = input("Set your y goal:")
                distance_tolerance = input("Set your tolerance:")
                #Checks if the coordinates are reachable
                if x == 11 or y == 11:
                    print "The turtle moving range is 11x11, choose another value: \n"
                    continue
                else:
                    #Send the turtle to the goal position 
                    self.move2goal(x,y,distance_tolerance)
            
            else:
                #Breaks the code if the user doesnt press Enter
                break


if __name__ == '__main__':
    try:
        #Testing our function
        x = turtleChallenge()
        x.turtle_wait_for_goal()

    except rospy.ROSInterruptException: pass
