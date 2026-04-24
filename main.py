from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import io
from PIL import Image
import uvicorn

app = FastAPI(title="Tyre Detection API")

model = YOLO("runs/detect/TyreDetection_Project/exp_v1_yolov8s/weights/best.pt")

@app.get("/")
def read_root():
    return {"message": "Tyre Detection API ishlamoqda! /docs sahifasiga o'ting."}


@app.post("/predict")
async def predict_tyre(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Model orqali bashorat qilish
    results = model.predict(source=image)
    
    predictions = []
    for r in results:
        for box in r.boxes:
            conf = float(box.conf)
            cls = int(box.cls)
            name = model.names[cls]
            predictions.append({
                "class_name": name,
                "confidence": round(conf, 2)
            })

    return {"filename": file.filename, "predictions": predictions}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)