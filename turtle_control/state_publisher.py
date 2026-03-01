import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtle_control.msg import TurtleState


class StatePublisher(Node):
    def __init__(self):
        super().__init__('state_publisher')

        self.pub = self.create_publisher(
            TurtleState,
            '/turtle_state',
            10
        )

        self.sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback,
            10
        )

    def callback(self, pose):
        msg = TurtleState()
        msg.x = pose.x
        msg.y = pose.y
        msg.theta = pose.theta
        msg.moving = True

        self.pub.publish(msg)


def main():
    rclpy.init()
    node = StatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
