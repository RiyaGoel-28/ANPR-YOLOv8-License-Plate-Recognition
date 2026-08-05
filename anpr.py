from ultralytics import YOLO
import easyocr
import cv2

# Load license plate detection model
plate_model = YOLO("plate_model/best.pt")

# Load OCR
reader = easyocr.Reader(['en'])

# Read image
image = cv2.imread("images/test.jpg")

# Detect number plates
results = plate_model(image)

for result in results:
    boxes = result.boxes

    for box in boxes:

        # Get plate coordinates
        x1, y1, x2, y2 = box.xyxy[0]

        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Crop plate
        plate = image[y1:y2, x1:x2]

        # OCR
        text = reader.readtext(plate)

        for t in text:
            print("Number Plate:", t[1])

        # Show plate
        cv2.imshow("Number Plate", plate)

cv2.waitKey(0)
cv2.destroyAllWindows()