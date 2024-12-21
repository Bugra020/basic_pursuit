import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Point


class ActionControl(Node):
    def __init__(self):

        super().__init__("action_control")

        self.start_pos = [0.0, 0.0]
        self.pos = self.start_pos
        self.pos_num = 0.0
        self.dest = self.start_pos

        self.subsciption = self.create_subscription(
            Point, "destination", self.get_destination, 10
        )

        self.publisher_ = self.create_publisher(Point, "position", 10)
        
        while self.dest[0] == 0.0 and self.dest[1] == 0.0:
            self.publish_pos()

    def get_destination(self, dest):
        self.get_logger().info(f"new destination: {dest.x},{dest.y}")

        while int(self.pos[0]) != int(dest.x) or int(self.pos[1]) != int(dest.y):
            self.update_pos(dest.x, dest.y)

    def update_pos(self, dx, dy):
        if int(self.pos[0]) != int(dx):
            self.pos[0] += int(dx - self.pos[0]) / abs(dx - self.pos[0])
        if int(self.pos[1]) != int(dy):
            self.pos[1] += int(dy - self.pos[1]) / abs(dy - self.pos[1])

        self.publish_pos()

    def publish_pos(self):
        pos = Point()
        pos.x = self.pos[0]
        pos.y = self.pos[1]
        pos.z = self.pos_num
        self.pos_num += 1

        self.publisher_.publish(pos)
        self.get_logger().info(f"{int(pos.z)}th pos: {pos.x},{pos.y}")


def main(args=None):
    rclpy.init(args=args)

    action_control = ActionControl()
    rclpy.spin(action_control)

    action_control.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
