# Multi-Object Video Tracking (MOT) & Interpolation Rubric

**Author:** Yvonne Obi (AI Data Evaluation Specialist)  
**Target Domain:** Autonomous Vehicle Front-Facing Dashcam Telemetry  

---

## 1. Keyframe Interpolation Protocols
- **Keyframe Spacing:** Keyframes must be manually placed at a maximum interval of **15 frames** (0.5s at 30 FPS) for linear trajectories, and every **5 frames** during rapid maneuvers or turns.
- **Occlusion Handling:**
  - **Temporary Occlusion (<1.0s):** Maintain `Track_ID` continuity across obscured frames using predicted linear motion interpolation.
  - **Permanent Re-appearance (>1.0s):** Terminate the original `Track_ID` and spawn a new ID upon re-entry into the frame view.

<Image src="image_agent_tag_3547723137061826751" alt="Sequence frame prediction and motion feature tracking diagram" caption="Temporal trajectory tracking and sequence forecasting" />

---

## 2. Temporal State Taxonomy

1. `Action_Start`: Frame where an object initiates crosswalk entry or lane change.
2. `In_Motion`: Continuous uniform motion across intermediate frames.
3. `Stationary_Sidewalk`: Object velocity is 0 m/s relative to ground context.
4. `Action_Stop`: Object halts at signal or crosswalk boundary.
