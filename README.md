# 🏎️ Tyre Error Proofing System using YOLOv8

This project provides an end-to-end computer vision pipeline to automate tyre quality control. It detects and classifies four specific types of wheels/tyres in a manufacturing environment.

---

## 📂 1. Dataset Information
The model was trained on a high-quality dataset consisting of **39,910 4K images**. 
- **Source:** I can't upload my dataset because of size it is 66.05 GB   
- **Classes:** `80_label`, `black_wheel`, `simple_wheel`, `white_wheel`.
- **Note:** Due to storage limits, only a sample dataset is included in this repository for testing purposes.

---

## 🛠️ 2. Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sizning_nikingiz/Tyre-Detection-Project.git](https://github.com/sizning_nikingiz/Tyre-Detection-Project.git)
   cd Tyre-Detection-Project

   ## 🚀 3. How to Run Inference (FastAPI)
This project includes a real-time API built with FastAPI to serve the model.

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

   python main.py
   
## 🐳 How to Run with Docker
To build and run this project in a container:
1. **Build:** `docker build -t tyre-detection .`
2. **Run:** `docker run -p 8000:8000 tyre-detection`
3. **Open:** Go to `http://localhost:8000/docs` to test the API.
