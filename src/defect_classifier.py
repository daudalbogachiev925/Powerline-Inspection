import cv2
import numpy as np

class DefectClassifier:
    """Простой rule-based классификатор дефектов изоляторов."""
    def classify(self, crop):
        if crop.size == 0:
            return "unknown", 0.0
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edge_density = edges.mean() / 255.0
        if edge_density > 0.3:
            return "crack", edge_density
        if gray.std() > 60:
            return "corrosion", gray.std() / 255
        return "ok", 1.0 - edge_density
