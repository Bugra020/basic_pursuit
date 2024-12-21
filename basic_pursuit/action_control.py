import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Point


class ActionControl(Node):
    def __init__(self):

        super().__init__("action_control")

        self.start_pos = [0, 0]
        self.pos = self.start_pos
        self.pos_num = 0

        self.subsciption = self.create_subscription(
            Point, "destination", self.get_destination, 10
        )

        #self.publisher = self.create_publisher(Point, "position", 10)

    def get_destination(self, dest):
        self.get_logger().info(f"new destination: {dest.x},{dest.y}")

def main(args=None):
    rclpy.init(args=args)

    action_control = ActionControl()
    rclpy.spin(action_control)

    action_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
