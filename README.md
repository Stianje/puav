# puav
Overhead object detection using YOLOv7 and DeepSORT

The intention of this project is to create an object detection system with YOLOv7 that can identify pedestrians,
cars, and other objects. We are using the Stanford campus drone data set to train our algorithm which is then
used to output the tracking data. We originally intended to count the people entering and exiting the frame, but
as a result of jittery object tracking, we decided to rather visualize the data in aggregate. Resulting in a trace of
the paths of different objects in the frame using Deepsort algorithm.

# Results
Coupa2 and Hyang0 scene from SDD Data set<br />

![Coupa2 Scene](https://github.com/Stianje/puav/blob/main/SDD_Yolov7__Deepsort.gif)
![Hyang0 Scene](https://github.com/Stianje/puav/blob/main/SDD_Yolov7__Deepsort_2.gif)

Heatmap generated from Hyang0 run
![Hyang0 Heatmap](https://github.com/Stianje/puav/blob/main/heat_map_alpha.png)
Blue: pedestrian<br />
Red: biker<br />
Green: cart

# Intro of folder structure.
```
Project_trainings - Producing the training data (Annotations And Video to frames)
Projectv2 - Main object neural network detector with trakcing, Yolov7 with Implemented Deepsort for tracking
Movemap - Creating of movemap from deepsort tracking
Count_Objects - Counting of different ids given by deepsort from labels file and comparing to dataset value
```

# Acknowledgements
https://github.com/WongKinYiu/yolov7<br />
https://github.com/haroonshakeel/yolov7-object-tracking<br />
https://cvgl.stanford.edu/projects/uav_data/
