import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Point
import random


class PathPublisher(Node):

    def __init__(self):
        super().__init__("path_publisher")
        self.publishler_ = self.create_publisher(Point, "destination", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.send_destination)
        self.dest_num = 0

    def send_destination(self):
        dest = Point()
        dest.x = random.random() * 100
        dest.y = random.random() * 100
        dest.z = float(self.dest_num)

        self.publishler_.publish(dest)
        self.get_logger().info(
            f"published dest :{dest.x:.2f},{dest.y:.2f}. destinaion number:{int(dest.z)}"
        )

        self.dest_num += 1


def main(args=None):
    rclpy.init(args=args)

    path_publisher = PathPublisher()

    rclpy.spin(path_publisher)

    path_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
