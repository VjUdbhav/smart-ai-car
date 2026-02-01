import cv2
from ultralytics import YOLO
from src.database import save_detection

model = YOLO("yolov8n.pt")  # lightweight model

def detect_damage(frame):
    results = model(frame)
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if conf > 0.5:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.putText(frame,"Damage",(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    return frame
