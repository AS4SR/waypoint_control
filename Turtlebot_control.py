#!/usr/bin/env python
import rospy  
import roslib
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetModelState



def get_state_call(model_name):
    try:
        return get_model_state(model_name = model_name)
    except rospy.ServiceException as e:
        print e



def setmodel():

    pub = rospy.Publisher('Turtlebot_control', ModelState, queue_size=10)
    rospy.init_node('set_model_state', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():

        
        modelstate = get_state_call("crumb_laberinto")

        cmd = ModelState()  
        cmd.twist.linear.x = 0.1
        cmd.twist.linear.y = 0
        cmd.twist.linear.z = 0
        cmd.twist.angular.x = 0.0
        cmd.twist.angular.y = 0.0
        cmd.model_name = "crumb_laberinto"
        pub.publish(cmd)
        rate.sleep()


if __name__ == '__main__':

    get_model_state = rospy.ServiceProxy('Turtlebot_control', GetModelState)
    try:
         setmodel()
    except rospy.ROSInterruptException:
         pass
