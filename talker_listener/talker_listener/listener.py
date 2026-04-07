import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node): 
    def __init__(self): 
        super().__init__('listener')
        self.subscriber = self.create_subscription(String, 'chatter', self.sub_cb, 10)

    def sub_cb(self, msg): 
        self.get_logger().info(f"I heard: {msg.data}")
        
def main(args=None):
    rclpy.init(args=args)

    listener = Listener()

    try: 
        rclpy.spin(listener)
    except KeyboardInterrupt:
        pass 
    finally: 
        if rclpy.ok(): 
            rclpy.shutdown()
        listener.destroy_node()

if __name__=="__main__": 
    main()