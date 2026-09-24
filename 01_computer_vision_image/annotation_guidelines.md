# Computer Vision Annotation Guidelines & Edge-Case Taxonomy

**Author:** Yvonne Obi (AI Data Evaluation Specialist)  
**Dataset Standard:** COCO Object Detection & Instance Segmentation  
 

## 1. Tight Bounding Box Rules
- **Pixel-Tight Fit:** Bounding boxes must enclose all visible pixels of the target object without excess background padding.
- **Occlusion Threshold:** Objects occluded greater than 80% should be tagged with `occlusion_level: "severe"` but kept within the dataset unless fewer than 10 pixels remain distinguishable.
- **Truncation Boundaries:** Objects cut off by image edges must maintain tight box borders along the image boundary frame without extrapolation beyond the canvas.

<Image src="image_agent_tag_3547723137061830398" alt="Data quality and precision layers in computer vision annotations" caption="Annotation precision and quality breakdown" />



## 2. Category Taxonomy & Edge Cases

| Class Name | Target Entities | Edge-Case Rule |
| :--- | :--- | :--- |
| `Pedestrian_Occluded` | Humans, children, standing/walking | Must capture partial limbs behind street furniture. |
| `Vehicle_Car` | Sedans, SUVs, trucks, buses | Includes parked vehicles if wheels are visible on pavement. |
| `Traffic_Sign_SpeedLimit` | Regulatory speed limit signs | Do not annotate sign posts/poles—only the sign face container. |
| `Vulnerable_Road_User_Cyclist` | Cyclists mounted on bicycles | Annotate person + bicycle as a single fused unit under this class. |



## 3. Quality Assurance & Error Metrics
- **Intersection over Union (IoU):** Benchmark target is **IoU ≥ 0.88** against gold-standard master annotator labels.
- **Category Confusion Matrix:** Zero tolerance for class misclassifications between human subjects and static background elements.
