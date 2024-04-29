from ultralytics import YOLO
import cv2


model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("C:/Users/Arthur/Documents/YOLO_Learning/RunningYolo/Images/street.jpg", show=True)
cv2.waitKey(0)

