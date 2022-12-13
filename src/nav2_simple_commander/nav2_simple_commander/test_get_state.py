
from audioop import getsample
from lifecycle_msgs.srv import GetState

import sys
import rclpy
from rclpy.node import Node
import time


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(GetState, '/amcl/get_state')
        

    def send_request(self):
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetState.Request()
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future, timeout_sec = 10)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()

    """循环获取state"""
    # rate = minimal_client.create_rate(1000)
    while 1:
        response = minimal_client.send_request()
        minimal_client.get_logger().info('current_state => id: {0} , label: {1}'.format(response.current_state.id, response.current_state.label))
        time.sleep(1)

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

