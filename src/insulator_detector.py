from ultralytics import YOLO

class InsulatorDetector:
    def __init__(self, model_path="yolov8n.pt", conf=0.4):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        res = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        return [{
            "bbox": b.xyxy[0].tolist(),
            "conf": float(b.conf[0]),
            "cls": self.model.names[int(b.cls[0])]
        } for b in res.boxes]
