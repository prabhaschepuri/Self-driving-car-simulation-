# Self-Driving Car Using Behavioral Cloning

This project implements an end-to-end autonomous driving system using Behavioral Cloning and Deep Learning. A Convolutional Neural Network (CNN) is trained on driving data collected from the Udacity Self-Driving Car Simulator to predict steering angles directly from camera images.

The model learns driving behavior by observing human driving demonstrations and then autonomously controls the vehicle in the simulator. The project includes data collection, image preprocessing, data augmentation, model training, and real-time deployment using Flask, Socket.IO, and Eventlet.

This project implements Behavioral Cloning for autonomous driving using a CNN trained on driving data collected from the [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim/releases).

## Features

Behavioral Cloning for autonomous steering control

CNN-based end-to-end learning

Image preprocessing and normalization

Data augmentation using left/right camera correction and image flipping

Real-time inference and vehicle control

Integration with the Udacity Self-Driving Car Simulator


[Driving_log_dataset](driving_log_3_cleaned.csv)  : Raw image dataset with image paths of center ,left,right cameras and with steering angle ,speed

[Libraries](Libraries.py) : Required Libraries

[Self driving car pic](Self%20driving%20car%20pic.png): Autonomous mode Simulation picture

[Preprocessing functions](driving_log_3_cleaned.csv) : Preprocessing functions for original images and augmented images(flipped images)

[MobileNetV2_model](MobileNetV2_model.py) : Pretrained 1000 class image classifier uses Depthwise separable convolutions which reduces computation

[Image_to_array_processing](Image%20to%20array%20processing.py) : Preprocessing the dataset and appending to the X and Y arrays

[Train_test split](Train_test%20split.py): Splitting the training and testing data

[Fine_tuning_model](Fine_tuning_model.py) : Extracting the output layers of MobileNetV2 architecture and adding the fully connected layers and pooling layers with single output layer(Steering angle) and fine tuning the model in training phase

[Autonomous mode](drive.py) : The communication between Udacity simulator and python logic built by using the socketio server and continous transmission of data between simulator and model predictions occurs,and car drives in autonomous mode 

<img width="1372" height="855" alt="image" src="https://github.com/user-attachments/assets/6b2fa080-fb6d-478f-8bab-5a88cbdb4329" />














