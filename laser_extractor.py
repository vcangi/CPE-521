"""
Authors: Andrew Alvarez, Vincent Cangiarella, Mitchell Dull


"""
import pandas as pd
import rospy
import tf
from sensor_msgs.msg import LaserScan
import geometry_msgs.msg
import tf.msg

def read_laser(file_name, front_rear) #indicated the file and which laser it is to pull data from
