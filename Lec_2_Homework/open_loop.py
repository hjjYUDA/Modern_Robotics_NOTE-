import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from math import pi


class Turtlebot(Node):
    def __init__(self):
        super().__init__("turtlebot_move")
        self.get_logger().info("Press Ctrl + C to terminate")

        # Publisher for cmd_vel topic
        self.vel_pub = self.create_publisher(Twist, "cmd_vel", 10)

        # Timer to execute run method periodically
        self.counter = 0
        self.timer = self.create_timer(0.1, self.run)  # 10 Hz timer

    def run(self):
        vel = Twist()

        ########### Here is your code ###########

        vel.linear.x = 0.5
        vel.angular.z = 0.0

        # Publish the velocity command
        self.vel_pub.publish(vel)
        self.counter += 1

        # Stop the robot and terminate
        self.get_logger().info("Action completed. Shutting down...")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    try:
        turtlebot = Turtlebot()
        rclpy.spin(turtlebot)
    except KeyboardInterrupt:
        turtlebot.get_logger().info("Action terminated.")
    finally:
        turtlebot.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
