import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav2_msgs.action import NavigateToPose


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
             NavigateToPose.Impl.FeedbackMessage,
            '/navigate_to_pose/_action/feedback',
            self.listener_callback,
            0)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        self.get_logger().info('current pose: ("%f", "%f")' %(msg.feedback.current_pose.pose.position.x, msg.feedback.current_pose.pose.position.y))


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