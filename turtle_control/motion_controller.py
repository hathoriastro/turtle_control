import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import tty
import termios
import threading


class MotionController(Node):
    def __init__(self):
        super().__init__('motion_controller')

        self.cmd_pub = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.linear_speed = 2.0
        self.angular_speed = 1.5

        self.keys_pressed = set()

        self.timer = self.create_timer(0.1, self.pose_callback)

        self.kb_thread = threading.Thread(target=self.read_keyboard, daemon=True)
        self.kb_thread.start()

        self.get_logger().info("WASD to move, Q to quit.")

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def read_keyboard(self):
        while rclpy.ok():
            key = self.get_key()
            if key == 'q':
                self.get_logger().info("Quitting...")
                rclpy.shutdown()
                break
            elif key in ('w', 'a', 's', 'd'):
                self.keys_pressed = {key}
            else:
                self.keys_pressed = set()

    def pose_callback(self):
        cmd = Twist()

        if 'w' in self.keys_pressed: # Ini contoh untuk maju, 
            cmd.linear.x = self.linear_speed # buat contoh lain untuk mundur, kiri, kanan

        self.cmd_pub.publish(cmd)


def main():
    rclpy.init()
    node = MotionController()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()