from ultralytics import YOLO
import cv2


model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("C:/Users/Arthur/Documents/YOLO_Learning/YOLO/RunningYolo/Images/cars1.jpg", show=True)
cv2.waitKey(0)

