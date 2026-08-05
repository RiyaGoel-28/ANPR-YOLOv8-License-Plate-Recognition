from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

image = cv2.imread("images/test.jpg")

results = model(image)

output = results[0].plot()

cv2.imshow("YOLO Detection", output)

cv2.waitKey(0)
cv2.destroyAllWindows()