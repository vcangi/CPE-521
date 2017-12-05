''' Parses IMU csv file and returns an array to be added to bag file
'''

import pandas as pd
import rospy
import tf
from sensor_msgs.msg import Imu
import geometry_msgs.msg
import tf.msg

def read_imu(file_name):
    data_no_headers = pd.read_csv(file_name, skiprows=0, nrows=1)
    cnt = 0

    t_odom_msgs = []
    imu_msgs = []

    for i in range(0,1):
        d_frame = data_no_headers.values
        t1 = rospy.Time.from_sec(float(d_frame[0,0]))

        angles = tf.transformations.quaternion_from_euler(0,0,0)
        imu  = Imu()
        imu.header.seq = cnt
        imu.header.stamp = t1
        imu.header.frame_id = "imu"
        imu.linear_acceleration.x = float(d_frame[0, 2]) # m/s^2
        imu.linear_acceleration.y = float(d_frame[0, 3]) # m/s^2
        imu.linear_acceleration.z = float(d_frame[0, 4]) # m/s^2
        imu.angular_velocity.x = float(d_frame[0, 5])# rad/s
        imu.angular_velocity.y = float(d_frame[0, 6])# rad/s
        imu.angular_velocity.z = float(d_frame[0, 7])# rad/s
        imu.orientation_covariance[0] = float(d_frame[0, 11])
        imu.orientation_covariance[1] = float(d_frame[0, 12])
        imu.orientation_covariance[2] = float(d_frame[0, 13])
        imu.orientation_covariance[3] = float(d_frame[0, 14])
        imu.orientation_covariance[4] = float(d_frame[0, 15])
        imu.orientation_covariance[5] = float(d_frame[0, 16])
        imu.orientation_covariance[6] = float(d_frame[0, 17])
        imu.orientation_covariance[7] = float(d_frame[0, 18])
        imu.orientation_covariance[8] = float(d_frame[0, 19])





        tf_msg = tf.msg.tfMessage()
        geo_msg = geometry_msgs.msg.TransformStamped()
        geo_msg.header.stamp = t1
        geo_msg.header.seq = cnt
        geo_msg.header.frame_id = "imu"
        geo_msg.child_frame_id = "base_link"
        geo_msg.transform.translation.x = -0.192
        geo_msg.transform.translation.y = -0.007
        geo_msg.transform.translation.z = 0.537

        geo_msg.transform.rotation.x = angles[0]
        geo_msg.transform.rotation.y = angles[1]
        geo_msg.transform.rotation.z = angles[2]
        geo_msg.transform.rotation.w = angles[3]

        tf_msg.transforms.append(geo_msg)
        imu_msgs.append(imu)

        cnt = cnt + 1
        data_no_headers = pd.read_csv(file_name, skiprows=cnt, nrows=1)
    return t_odom_msgs, imu_msgs



if __name__ == '__main__':
    read_imu("Bicocca_2009-02-25b-IMU_STRETCHED.csv")
