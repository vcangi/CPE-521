import rosbag, rospy
from odometry_extractor import read_odometry
from laser_extractor import read_laser
from rear_laser_extractor import read_rear_laser
rospy.init_node('data_saver')

