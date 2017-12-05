#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Reads and stores data for all topics

@author: mfahad
"""


import rosbag, rospy
from odometry_extractor import read_odometry
from laser_extractor import read_laser
from rear_laser_extractor import read_rear_laser
from imu_extractor import read_imu
rospy.init_node('data_saver')

def write_bagfile(data_set_name, odom_msgs, tf_msgs, t_lsr_f_msgs,laser_msgs,t_lsr_r_msgs,r_laser_msgs, t_imu_msgs, imu_msgs):
    ''' Write all ROS msgs, into the bagfile.
    '''
    bag = rosbag.Bag(data_set_name, 'w')
     #write the tf msgs into the bagfile
    for msg in tf_msgs:
        bag.write('/tf', msg, msg.transforms[0].header.stamp )
    # write the uwb msgs into the bagfile
    for msg in odom_msgs:
        bag.write('odom', msg, msg.header.stamp)

    for msg in t_lsr_f_msgs:
        bag.write('/tf', msg, msg.transforms[0].header.stamp )
    # write the uwb msgs into the bagfile
    for msg in laser_msgs:
        bag.write('front_laser', msg, msg.header.stamp)

    for msg in t_lsr_r_msgs:
        bag.write('/tf', msg, msg.transforms[0].header.stamp )
    # write the uwb msgs into the bagfile
    for msg in r_laser_msgs:
        bag.write('rear_laser', msg, msg.header.stamp)

    for msg in t_imu_msgs:
        bag.write('/tf', msg, msg.transforms[0].header.stamp)

    for msg in imu_msgs:
        bag.write('imu', msg, msg.header.stamp)

    bag.close()
    print "Finished Bagfile IO"


tf_msgs,odom_msgs = read_odometry()
t_lsr_f_msgs,laser_msgs = read_laser("Bicocca_2009-02-25b-SICK_FRONT.csv")
t_lsr_r_msgs,r_laser_msgs = read_rear_laser("Bicocca_2009-02-25b-SICK_REAR.csv")
t_imu_msgs, imu_msgs = read_imu("Bicocca_2009-02-25b-IMU_STRETCHED.csv")
write_bagfile("combined_updated2", odom_msgs, tf_msgs, t_lsr_f_msgs,laser_msgs,t_lsr_r_msgs,r_laser_msgs, t_imu_msgs, imu_msgs)
