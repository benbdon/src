#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyCustomNode(Node): # MODIFY Class name
    def __init__(self):
        super().__init__("node_name") # MODIFY node name, can be the same as filename, not required


def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() # COPY in class name from above
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()