import numpy as np
from src.line_detector import PowerLineDetector

def test_detect_returns_list():
    img = (np.random.rand(480, 640, 3) * 255).astype(np.uint8)
    assert isinstance(PowerLineDetector().detect(img), list)
