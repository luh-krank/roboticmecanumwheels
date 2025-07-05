# mecanum_bot

ROS Noetic navigation stack for a Mecanum-wheel robot with Jetson Nano, RP Lidar, Arduino + OSOYOO Mecanum Shield, and Intel RealSense D435i.

## 🚀 Features
- SLAM using RP Lidar
- Navigation & obstacle avoidance with `move_base`
- Serial control of Arduino mecanum motors
- RViz visualization
- RealSense camera support

## 🧰 Hardware
- Jetson Nano
- Arduino UNO + OSOYOO Mecanum Shield
- RP Lidar (A1/A2)
- Intel RealSense D435i

## 📦 Installation
```bash
cd ~/catkin_ws/src
git clone https://github.com/yourusername/mecanum_bot.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## 🎮 Usage
```bash
roslaunch mecanum_bot slam.launch
rosrun map_server map_saver -f ~/catkin_ws/src/mecanum_bot/maps/map
roslaunch mecanum_bot map_navigation.launch
```

## 🔧 Notes
- Arduino must be flashed with code to handle: `fwd`, `back`, `left`, `right`, `stop`
- Lidar on `/dev/ttyUSB0`, RealSense via USB 3.0

## 🧪 License
MIT
