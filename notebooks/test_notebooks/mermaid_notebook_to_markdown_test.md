<!-- TOC -->
# Table of Contents

- [Traffic Flow State Analysis](#traffic-flow-state-analysis)
- [Multi-Object Detection Pipeline](#multi-object-detection-pipeline)
- [Camera Calibration for Traffic Monitoring](#camera-calibration-for-traffic-monitoring)
- [Vehicle Speed Estimation](#vehicle-speed-estimation)
- [Lane Detection Using Hough Transform](#lane-detection-using-hough-transform)
- [Intersection Movement Analysis](#intersection-movement-analysis)

<!-- /TOC -->


## Traffic Flow State Analysis

Traffic flow exhibits three distinct phases based on density-velocity relationships: free flow (v = vmax), synchronized flow (reduced velocity with increasing density), and congested flow (stop-and-go waves).

```mermaid
stateDiagram-v2
    [*] --> FreeFlow: Low density
    FreeFlow --> Synchronized: Density threshold
    Synchronized --> Congested: Critical density
    Congested --> Synchronized: Density reduction
    Synchronized --> FreeFlow: Traffic clears
    
    FreeFlow: v = 65-80 mph
    Synchronized: v = 35-65 mph
    Congested: v = 0-35 mph
    
    note right of Congested: Shockwave formation
```

Fundamental relationship: q = k × v where q = flow (vehicles/hour), k = density (vehicles/mile), v = velocity (mph)

## Multi-Object Detection Pipeline

YOLO-based detection pipeline processes video frames at 30 FPS, achieving mAP@0.5 = 0.78 for vehicle detection across multiple classes.

```mermaid
flowchart LR
    A[Video Frame] --> B[Preprocessing]
    B --> C[YOLO Detector]
    C --> D{Confidence > 0.5?}
    D -->|Yes| E[NMS]
    D -->|No| F[Discard]
    E --> G[Kalman Filter]
    G --> H[Track Association]
    H --> I[Output Tracks]
    
    style C fill:#a5d6a7
    style G fill:#90caf9
    style I fill:#ffcc80
```

Detection classes: Car (0.85), Truck (0.78), Bus (0.81), Motorcycle (0.72), Bicycle (0.69)

## Camera Calibration for Traffic Monitoring

Intrinsic and extrinsic calibration achieves reprojection error < 0.5 pixels using Zhang's method with checkerboard patterns.

```mermaid
graph TD
    A[Checkerboard Images] --> B[Corner Detection]
    B --> C[2D-3D Correspondences]
    C --> D[Initial Guess]
    D --> E[Optimization Loop]
    E --> F{RMSE < 0.5px?}
    F -->|No| G[Refine Parameters]
    G --> E
    F -->|Yes| H[K, R, t matrices]
    H --> I[Undistort Images]
    
    style A fill:#e1bee7
    style H fill:#c5e1a5
    style I fill:#81c784
```

Calibration matrix K contains: focal length (fx=1832.4, fy=1835.7), principal point (cx=956.2, cy=542.8)

## Vehicle Speed Estimation

Optical flow-based speed estimation using Lucas-Kanade method achieves ±3 mph accuracy when calibrated with ground truth radar data.

```mermaid
graph LR
    A[Frame t] --> B[Feature Detection]
    A2[Frame t+1] --> B
    B --> C[Optical Flow]
    C --> D[Pixel Displacement]
    D --> E[Camera Calibration]
    E --> F[Real-world Speed]
    F --> G[Kalman Filter]
    G --> H[Smoothed Speed]
    
    style C fill:#b39ddb
    style F fill:#81c784
    style H fill:#4fc3f7
```

Speed = (pixel_displacement × scale_factor) / time_delta, where scale_factor = 0.142 m/pixel at 50m distance

## Lane Detection Using Hough Transform

Edge detection and probabilistic Hough transform identify lane markings with 94% accuracy under daylight conditions.

```mermaid
flowchart TD
    A[Input Frame] --> B[Grayscale]
    B --> C[Gaussian Blur]
    C --> D[Canny Edge]
    D --> E[ROI Mask]
    E --> F[Hough Lines]
    F --> G{Line Angle?}
    G -->|20°-70°| H[Valid Lane]
    G -->|Other| I[Reject]
    H --> J[Polynomial Fit]
    
    style D fill:#ffb74d
    style F fill:#64b5f6
    style J fill:#aed581
```

Parameters: Canny(50,150), Hough(ρ=1, θ=π/180, threshold=50, minLength=100, maxGap=50)

## Intersection Movement Analysis

Computer vision tracks turning movements at 4-way intersection, detecting conflicts with 89% precision using trajectory prediction.

```mermaid
graph TD
    A[Vehicle Detection] --> B[Trajectory Extraction]
    B --> C[Movement Classification]
    C --> D{Movement Type}
    D -->|Left Turn| E[Conflict Check]
    D -->|Through| F[Speed Analysis]
    D -->|Right Turn| G[Yield Detection]
    E --> H[Safety Score]
    F --> H
    G --> H
    
    style C fill:#ce93d8
    style H fill:#66bb6a
```

Hourly movements: Left=312, Through=847, Right=423. Critical conflicts: 17/hour (2.1% of turns)


```python

```
