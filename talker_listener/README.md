# ROS2 Talker-Listener Demo

A minimal ROS2 (Humble) package demonstrating the **publisher/subscriber** communication pattern using the `chatter` topic. This is a foundational example for understanding how nodes exchange messages through the ROS2 middleware.

---

## Package Structure

```
ros2_pubsub_demo/
├── __init__.py
├── talker.py       # Publisher node
└── listener.py     # Subscriber node
```

---

## Nodes

### Talker (`talker.py`)

A publisher node that broadcasts string messages on the `chatter` topic at a fixed rate.

| Property      | Value              |
|---------------|--------------------|
| Node name     | `talker_node`      |
| Topic         | `/chatter`         |
| Message type  | `std_msgs/String`  |
| Publish rate  | 2 Hz (every 0.5 s) |

**Behavior:** Publishes incrementing messages in the format `Hello world 0`, `Hello world 1`, etc.

---

### Listener (`listener.py`)

A subscriber node that listens to the `chatter` topic and logs every received message.

| Property      | Value              |
|---------------|--------------------|
| Node name     | `listener`         |
| Topic         | `/chatter`         |
| Message type  | `std_msgs/String`  |

**Behavior:** Prints each received message to the ROS2 logger: `I heard: Hello world N`.

---

## Communication Flow

```
┌─────────────────┐        /chatter        ┌──────────────────┐
│  talker_node    │ ─────────────────────► │    listener      │
│  (Publisher)    │   std_msgs/String @2Hz │  (Subscriber)    │
└─────────────────┘                        └──────────────────┘
```

---

## Usage

Make sure you have **ROS2 Humble** installed and your workspace sourced.

### 1. Build the package

```bash
colcon build --packages-select <your_package_name>
source install/setup.bash
```

### 2. Run the Talker

```bash
ros2 run <your_package_name> talker
```

### 3. Run the Listener (in a new terminal)

```bash
source install/setup.bash
ros2 run <your_package_name> listener
```

### 4. Inspect the topic (optional)

```bash
# List active topics
ros2 topic list

# Echo messages in real time
ros2 topic echo /chatter

# Check publish rate
ros2 topic hz /chatter
```

---

## Requirements

- ROS2 Humble Hawksbill
- Python 3.10+
- `rclpy`
- `std_msgs`

---

## References

- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [rclpy API Reference](https://docs.ros2.org/humble/api/rclpy/)
- [Writing a simple publisher and subscriber (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)