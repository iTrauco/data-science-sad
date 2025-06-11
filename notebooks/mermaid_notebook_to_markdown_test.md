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


```python

```
