"""
Authors: Andrew Alvarez, Vincent Cangiarella, Mitchell Dull

Based on work by mfahad
"""
import pandas as pd
import rospy
import tf
from sensor_msgs.msg import LaserScan
import geometry_msgs.msg
import tf.msg

def read_laser(file_name, front_rear) #indicated the file and which laser it is to pull data from
	#front_rear accepts "front_laser" and "rear_laser"
	data = pd.read_csv(file_name, skiprows = 0, nrows = 1)
	count = 0

	d_frame = data.values
	odom_msg = []
	laser_msg = []

	while len(data.values) >= 1:
		print count


  		t1 = rospy.Time.from_sec(float(d_frame[0,0]))
        d_frame = data_no_headers.values
        
        tf_msg = tf.msg.tfMessage()
        geo_msg = geometry_msgs.msg.TransformStamped()
        geo_msg.header.stamp = t1 
        geo_msg.header.seq = cnt
        geo_msg.header.frame_id = "base_link"
        geo_msg.child_frame_id = front_rear

        if front_rear == "front_laser"
	        geo_msg.transform.translation.x = 0.08
	        geo_msg.transform.translation.y = 0
	        geo_msg.transform.translation.z = 0.45
	        angles = tf.transformations.quaternion_from_euler(0,0,0)

	    else if front_rear == "rear_laser"
	        geo_msg.transform.translation.x = -0.463
	        geo_msg.transform.translation.y = 0.001
	        geo_msg.transform.translation.z = 0.454
	        angles = tf.transformations.quaternion_from_euler(0,0,-3.14) 
        
         
        geo_msg.transform.rotation.x = angles[0]
        geo_msg.transform.rotation.y = angles[1]
        geo_msg.transform.rotation.z = angles[2]
        geo_msg.transform.rotation.w = angles[3]
        tf_msg.transforms.append(geo_msg)
        odom_msg.append(tf_msg)


		scan = LaserScan()

        scan.header.seq = count
        scan.header.stamp = t1
        scan.header.frame_id = front_rear
    
        scan.angle_min = -1.57
        scan.angle_max = 1.57
        scan.angle_increment = 3.14 / 180
        scan.time_increment = (1.0 / 75.0)/181
        scan.range_min = 0.0
        scan.range_max = 30.0
        scan.ranges = []
        scan.intensities = []
        
        for j in range(3, 184):
            scan.ranges.append(float(d_frame[0,j]))  
        laser_msg.append(scan) 

        count = count + 1
        data = pd.read_csv(file_name, skiprows = count, nrows = 1)

    return odom_msg, laser_msg