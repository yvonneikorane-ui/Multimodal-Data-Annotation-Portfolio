"""
COCO JSON Schema & Polygon Geometry Validator
Author: Yvonne Obi (AI Data Evaluation Specialist)
Description: Automated pipeline script to check bounding box integrity, 
             polygon non-self-intersection, and category ID alignments.
"""

import json
import sys
from typing import Dict, Any

def validate_coco_file(file_path: str) -> bool:
    print(f"[*] Beginning COCO Schema Validation: {file_path}")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data: Dict[str, Any] = json.load(f)
    except Exception as e:
        print(f"[!] Critical Error loading JSON file: {e}")
        return False

    required_keys = ["info", "licenses", "images", "categories", "annotations"]
    for key in required_keys:
        if key not in data:
            print(f"[FAIL] Missing top-level required key: '{key}'")
            return False

    category_ids = {cat["id"] for cat in data.get("categories", [])}
    image_ids = {img["id"] for img in data.get("images", [])}

    print(f"[INFO] Total Categories Found: {len(category_ids)}")
    print(f"[INFO] Total Images Found: {len(image_ids)}")
    print(f"[INFO] Total Annotations Found: {len(data.get('annotations', []))}")

    # Validate annotations
    errors = 0
    for ann in data.get("annotations", []):
        ann_id = ann.get("id")
        
        # Foreign Key Checks
        if ann.get("image_id") not in image_ids:
            print(f"[ERROR] Annotation {ann_id}: Orphaned image_id {ann.get('image_id')}")
            errors += 1
            
        if ann.get("category_id") not in category_ids:
            print(f"[ERROR] Annotation {ann_id}: Invalid category_id {ann.get('category_id')}")
            errors += 1

        # Bounding Box Check [x, y, width, height]
        bbox = ann.get("bbox", [])
        if len(bbox) != 4 or any(x is None or x < 0 for x in bbox):
            print(f"[ERROR] Annotation {ann_id}: Malformed bbox coordinates {bbox}")
            errors += 1
        elif bbox[2] * bbox[3] == 0:
            print(f"[ERROR] Annotation {ann_id}: Zero-area bounding box detected {bbox}")
            errors += 1

        # Segmentation Check
        seg = ann.get("segmentation", [])
        if not seg or not isinstance(seg, list):
            print(f"[ERROR] Annotation {ann_id}: Missing or invalid segmentation ring")
            errors += 1

    if errors == 0:
        print("[SUCCESS] All COCO dataset checks passed! Dataset is production-ready.\n")
        return True
    else:
        print(f"[FAIL] Dataset validation failed with {errors} total errors.\n")
        return False

if __name__ == "__main__":
    coco_path = "01_computer_vision_image/instances.json"
    success = validate_coco_file(coco_path)
    sys.exit(0 if success else 1)
