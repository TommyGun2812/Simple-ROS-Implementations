import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

TIMER_PERIOD = 0.5 # 2Hz

class Talker(Node): 
    def __init__(self): 
        super().__init__('talker_node')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(TIMER_PERIOD, self.timer_cb)
        self.i = 0

    def timer_cb(self): 
        msg = String()
        msg.data = f"Hello world {self.i}"
        self.publisher.publish(msg)
        self.get_logger().info(f"I said: {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    talker = Talker()

    try: 
        rclpy.spin(talker)
    except KeyboardInterrupt:
        pass 
    finally: 
        if rclpy.ok(): 
            rclpy.shutdown()
        talker.destroy_node()

if __name__=="__main__": 
    main()