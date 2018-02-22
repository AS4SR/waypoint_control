#!/usr/bin/env python
import rospy  
import roslib
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
from gazebo_msgs.msg import LinkState
from gazebo_msgs.srv import GetModelState



def get_state_call(model_name):
    try:
        return get_model_state(model_name = model_name)
    except rospy.ServiceException as e:
        print e



def setmodel():

    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    pub1 = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=10)
    rospy.init_node('set_model_state', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():

        modelstate = get_state_call("crumb")
        #print modelstate
        cmd = ModelState()  
        link = LinkState()
        link.link_name = "wheel_left_link"
        link.twist.angular.y = 2
        link.reference_frame = "wheel_left_link"

        link1 = LinkState()
        link1.link_name = "wheel_right_link"
        link1.twist.angular.y = 2
        link1.reference_frame = "wheel_right_link"

        pub1.publish(link)
        #pub1.publish(link1)

        print link
        cmd.pose.position = modelstate.pose.position
        cmd.twist.linear.x = 0
        cmd.twist.linear.y = 0
        cmd.twist.linear.z = 0
        cmd.twist.angular.x = 0.0
        cmd.twist.angular.y = 0.0
        cmd.twist.angular.z = 0
        cmd.model_name = "crumb"
        #print cmd
        #pub.publish(cmd)
        rate.sleep()


if __name__ == '__main__':

    get_model_state = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    try:
         setmodel()
    except rospy.ROSInterruptException:
         pass
