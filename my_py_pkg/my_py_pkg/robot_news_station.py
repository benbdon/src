#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String #new import, make sure to update the package.xml


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") # MODIFY node name, can be the same as filename, not required
        self.robot_name_ = "C3PO"
        self.publisher_ = self.create_publisher(String, "robot_news",10) #added a publisher
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started.")

    def publish_news(self): #method for publishing
        msg = String()
        msg.data = "Hi, this is " + self.robot_name_ + " from the robot news station"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args) #initialize comms
    node = RobotNewsStationNode() # COPY in class name from above
    rclpy.spin(node) 
    rclpy.shutdown()


if __name__ == "__main__":
    main()