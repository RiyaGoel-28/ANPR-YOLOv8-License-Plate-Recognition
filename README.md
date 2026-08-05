# 🚗 YOLOv8 Based Automatic Number Plate Recognition System

## 📌 Overview

This project is an Automatic Number Plate Recognition (ANPR) system using YOLOv8 and EasyOCR.

The system detects license plates from vehicle images, extracts the plate number using OCR, and displays the result through a Streamlit web application.

## ✨ Features

- YOLOv8 based license plate detection
- EasyOCR based text recognition
- Streamlit web interface
- Image upload and prediction
- License plate bounding box detection

## 🛠️ Technologies Used

- Python
- YOLOv8
- EasyOCR
- OpenCV
- Streamlit
- PyTorch

## ▶️ Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## 📂 Main Files

- app.py - Streamlit web interface
- anpr.py - ANPR detection logic
- main.py - Main processing script
- plate_model/best.pt - YOLOv8 license plate model

## 👩‍💻 Author

Riya Goel

GitHub:
https://github.com/RiyaGoel-28
