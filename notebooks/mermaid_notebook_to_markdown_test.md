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


```python

```
