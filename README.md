# puav
Overhead object detection using YOLOv7 and DeepSORT

The intention of this project is to create an object detection system with YOLOv7 that can identify pedestrians,
cars, and other objects. We are using the Stanford campus drone data set to train our algorithm which is then
used to output the tracking data. We originally intended to count the people entering and exiting the frame, but
as a result of jittery object tracking, we decided to rather visualize the data in aggregate. Resulting in a trace of
the paths of different objects in the frame using Deepsort algorithm.

# Results
![](https://github.com/Stianje/puav/blob/main/SDD_Yolov7__Deepsort.gif)
![](https://github.com/Stianje/puav/blob/main/SDD_Yolov7__Deepsort_2.gif)
![](https://github.com/Stianje/puav/blob/main/heat_map_alpha final.png)

# Acknowledgements
https://github.com/WongKinYiu/yolov7<br />
https://github.com/haroonshakeel/yolov7-object-tracking<br />
https://cvgl.stanford.edu/projects/uav_data/
