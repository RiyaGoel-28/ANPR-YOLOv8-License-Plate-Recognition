import streamlit as st
from ultralytics import YOLO
import easyocr
import cv2
import numpy as np

# Load models
model = YOLO("plate_model/best.pt")
reader = easyocr.Reader(['en'])

st.title("YOLOv8 Based Automatic Number Plate Recognition System")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    results = model(image)

    for result in results:
        for box in result.boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            plate = image[y1:y2, x1:x2]

            text = reader.readtext(plate)

            number = ""

            for t in text:
                number += t[1] + " "

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

            st.success(
                "Number Plate: " + number
            )

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    st.image(
        image,
        caption="Detected Result"
    )