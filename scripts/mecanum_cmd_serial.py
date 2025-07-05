#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def callback(msg):
    x = msg.linear.x
    y = msg.linear.y
    z = msg.angular.z

    if x > 0:
        ser.write(b'fwd\n')
    elif x < 0:
        ser.write(b'back\n')
    elif y > 0:
        ser.write(b'left\n')
    elif y < 0:
        ser.write(b'right\n')
    elif z > 0:
        ser.write(b'rotate_left\n')
    elif z < 0:
        ser.write(b'rotate_right\n')
    else:
        ser.write(b'stop\n')

rospy.init_node('mecanum_cmd_serial')
rospy.Subscriber('/cmd_vel', Twist, callback)
rospy.spin()
