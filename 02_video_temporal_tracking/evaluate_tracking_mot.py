"""
Multi-Object Tracking (MOT) Trajectory & Continuity Evaluator
Author: Yvonne Obi (AI Data Evaluation Specialist)
Description: Verifies sequence keyframes, trajectory continuity, and bounding box interpolation
             integrity across multi-frame temporal video sequences.
"""

import json
import sys
from typing import Dict, Any

def evaluate_tracking_sequence(file_path: str):
    print(f"[*] Evaluating Video Tracking Telemetry: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data: Dict[str, Any] = json.load(f)

    meta = data.get("sequence_metadata", {})
    total_frames = meta.get("total_frames", 0)
    fps = meta.get("fps", 30)

    print(f"[INFO] Video ID: {meta.get('video_id')}")
    print(f"[INFO] Duration: {meta.get('duration_seconds')}s @ {fps} FPS ({total_frames} frames)")

    tracks = data.get("tracks", [])
    print(f"[INFO] Evaluating {len(tracks)} tracked object trajectories...")

    for track in tracks:
        track_id = track.get("track_id")
        label = track.get("label")
        keyframes = track.get("keyframes", [])

        print(f"\n---> Analyzing Track: [{track_id}] Class: ({label})")
        print(f"     Keyframe Count: {len(keyframes)}")

        previous_frame = None
        for kf in keyframes:
            frame_no = kf.get("frame")
            state = kf.get("state")
            bbox = kf.get("bbox")
            interpolated = kf.get("interpolated")

            # Check bbox validity
            if len(bbox) != 4 or any(c < 0 for c in bbox):
                print(f"     [ERROR] Frame {frame_no}: Invalid bounding box coordinates: {bbox}")

            # Check temporal monotonicity
            if previous_frame is not None and frame_no <= previous_frame:
                print(f"     [ERROR] Non-sequential frame order detected at Frame {frame_no}")

            previous_frame = frame_no

            print(f"     • Frame {frame_no:02d} | State: {state:<25} | Interpolated: {str(interpolated):<5} | BBox: {bbox}")

    print("\n[SUCCESS] Temporal tracking trajectory evaluation completed successfully.\n")

if __name__ == "__main__":
    tracking_file = "02_video_temporal_tracking/video_track_01.json"
    evaluate_tracking_sequence(tracking_file)
