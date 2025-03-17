#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node): #inherits all ROS2 functionality from the Node class

    def __init__(self): #constructor 
        super().__init__("py_test") #calls the parent constructor
        self.counter_ = 0 #initialize attribute and use trailing underscore by convetion
        self.get_logger().info("Hello world")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello aaaas" + str(self.counter_))
        self.counter_ += 1
        
def main(args=None):
    rclpy.init(args=args) #still initialize comms
    node = MyNode() #create node
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()