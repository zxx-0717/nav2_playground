import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('sub_amcl')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info("test1234")
        self.get_logger().info("amcl_x: {0}, amcl_y: {1}\n".format(msg.pose.pose.position.x, msg.pose.pose.position.y))
        self.get_logger().info("loggername: {}\n".format(self._logger.name))


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()