import cv2
import numpy as np

class PowerLineDetector:
    """Детекция проводов через LSD (Line Segment Detector) + Hough."""
    def __init__(self, min_length=80):
        self.lsd = cv2.createLineSegmentDetector(0)
        self.min_length = min_length

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        lines = self.lsd.detect(gray)[0]
        if lines is None:
            return []
        result = []
        for l in lines:
            x1, y1, x2, y2 = l[0]
            length = np.hypot(x2 - x1, y2 - y1)
            if length >= self.min_length:
                result.append([float(x1), float(y1), float(x2), float(y2), length])
        return result
