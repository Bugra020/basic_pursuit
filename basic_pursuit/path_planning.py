import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Point
import random


class PathPublisher(Node):

    def __init__(self):
        super().__init__("path_publisher")
        self.publishler_ = self.create_publisher(Point, "destination", 10)

        self.subscription = self.create_subscription(
            Point, "position", self.send_destination, 10
        )

        self.dest = [0.0, 0.0]
        self.dest_num = 1

    def check_pos(self, pos):
        if (int(pos.x) == int(self.dest[0])) and (int(pos.y) == int(self.dest[1])):
            return True
        else:
            return False

    def send_destination(self, pos):
        self.get_logger().info(f"x:{pos.x},y:{pos.y}")
        dest = Point()
        dest.x = self.dest[0]
        dest.y = self.dest[1]

        if self.check_pos(pos):
            dest = self.new_dest()
            self.dest[0] = dest.x
            self.dest[1] = dest.y
            self.get_logger().info(
                f"published dest :{dest.x:.2f},{dest.y:.2f}. destinaion number:{int(dest.z)}"
            )
            self.dest_num += 1

            self.publishler_.publish(dest)

    def new_dest(self):
        dest = Point()
        dest.x = self.dest[0] = float(int(random.random() * 100))
        dest.y = self.dest[1] = float(int(random.random() * 100))
        dest.z = float(self.dest_num)

        return dest


def main(args=None):
    rclpy.init(args=args)

    path_publisher = PathPublisher()

    rclpy.spin(path_publisher)

    path_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
