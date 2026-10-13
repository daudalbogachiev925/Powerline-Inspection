import json
from datetime import datetime

class GeoTagger:
    def __init__(self, path="defects.geojson"):
        self.path = path
        self.features = []

    def add(self, lat, lon, defect_type, confidence, image_path):
        self.features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {
                "type": defect_type,
                "confidence": confidence,
                "image": image_path,
                "timestamp": datetime.utcnow().isoformat()
            }
        })

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump({"type": "FeatureCollection",
                       "features": self.features}, f, ensure_ascii=False, indent=2)
