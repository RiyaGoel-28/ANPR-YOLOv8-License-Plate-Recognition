import easyocr
import cv2

# Load OCR model
reader = easyocr.Reader(['en'])

# Read image
image = cv2.imread("images/test.jpg")

# Detect text
result = reader.readtext(image)

# Print detected text
for text in result:
    print(text[1])