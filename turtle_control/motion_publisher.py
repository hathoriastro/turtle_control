import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MotionPublisher(Node):
    def __init__(self):
        super().__init__('motion_publisher')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(0.5, self.publish_cmd)

    def publish_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing velocity command')


def main():
    rclpy.init()
    node = MotionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
