## Overview

This project aims to automate the process of sorting and classifying potatoes by size as they move along a conveyor belt. By leveraging image processing techniques with OpenCV and a Convolutional Neural Network (CNN) algorithm, we achieve real-time categorization of potatoes, significantly minimizing manual labor and enhancing automation in line with Industry 4.0 principles.

## Project Workflow

1. **Potato Detection**: The system identifies whether the vegetable on the conveyor belt is a potato. 
2. **Image Capture and Processing**: A high-definition camera captures images of the potato in motion. The images are processed to generate contours around the moving objects.
3. **Size Classification**: Based on the calculated contour area, the potatoes are categorized by size.
4. **Conveyor Belt System**: The conveyor belt is equipped with:
   - **High-definition Camera**: For capturing images of the potatoes.
   - **Ultrasonic Sensors**: For detecting the presence of potatoes.
   - **Servo-Motor Operated Arms**: Controlled by an Arduino microcontroller, the servo arms guide the potatoes to designated containers based on their size.

## Implementation Details

- **Image Processing**: The OpenCV module in Python is used to process each frame and detect the contours of the potatoes.
- **CNN Algorithm**: A Convolutional Neural Network is employed to classify the potatoes based on their size, using the contour area as the primary metric.
- **Hardware Integration**: The system integrates various hardware components, including an Arduino microcontroller, servo motors, ultrasonic sensors, and a camera.

<p align="center">
  <img src="https://github.com/niteshsilwal01/Automatic-Potato-Segregation/blob/main/images/Process%20Flowchart.png?raw=true" alt="Process Flowchart">
</p>


## Goals

- **Minimize Manual Labor**: Automate the sorting process to reduce human intervention.
- **Enhance Automation**: Improve the efficiency and accuracy of the classification system.
- **Apply Industry 4.0 Concepts**: Leverage advanced technologies to create a smart, automated sorting system.

## Hardware Components

- **Arduino Microcontroller**: Controls the servo motors and sensors.
- **High-definition Camera**: Captures real-time images of the potatoes.
- **Ultrasonic Sensors**: Detects the presence and position of potatoes on the conveyor belt.
- **Servo Motors**: Operates the arms that direct potatoes to different containers.

## Software Components

- **Python OpenCV**: Used for image processing and contour detection.
- **CNN Model**: Classifies the potatoes by size based on contour analysis.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/niteshsilwal01/Automatic-Potato-Segregation.git
   ```
2. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Script**:
   ```bash
   python main.py
   ```

## Future Enhancements

- Integrate additional sensors for better detection accuracy.
- Implement machine learning models for enhanced classification.
- Expand the system to classify multiple types of vegetables.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.