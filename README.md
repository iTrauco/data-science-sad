# Multi-Object Tracking Computer Vision System Design Proposal

> **Note**: This is a personal repository for developing a systematic approach to data science, AI, and ML system engineering using information systems analysis and design principles. The source of truth for work completed in this repository is located in the notebook within the `notebooks/` directory, not in this README.

> **Branch Scope**: All work for this project is scoped to the `traffic-vision/multi-object-tracking` branch only.

> **Clean Rebuild No. 2**: This is a clean rebuild of the traffic-vision systems analysis and design proposal originally developed in [`scenario06/traffic-vision/multi-object-tracking`](https://github.com/iTrauco/data-science-sad/tree/scenario06/traffic-vision/multi-object-tracking), incorporating refined workflow architecture.

## Scenario Overview
A transportation research team wants to analyze traffic camera footage to detect and track vehicles across multiple highway locations. They want to use computer vision models with optimization for deployment but struggle with handling streaming video data, model compression, and inference pipeline design and are unsure where to start. They have access to an HPC workstation with GPU and GCP for video storage and pipeline processing. This proposal outlines a systems approach for model development, data handling, and evaluation-including infrastructure recommendations for scalability and reproducibility.

## Proposal Framework
This Jupyter notebook presents a systems analysis and design approach to the multi-object tracking computer vision challenge. The proposal follows established information systems design principles, emphasizing:
- **Video Processing Architecture**: Methodical approach to streaming data and computational requirements
- **Data Pipeline Design**: Structured approach to annotation, preprocessing, and training workflows
- **Model Optimization Strategy**: Process-oriented approach to architecture selection and deployment
- **System Evaluation Framework**: Comprehensive methodology for performance assessment and validation

## System Components
The proposed solution addresses the following key subsystems:
1. **Data Processing Subsystem**
   - Video streaming and frame extraction
   - Pre-processing pipeline design
   - Data format standardization

2. **Data Annotation Framework**
   - Annotation tool integration and workflow
   - Label format specifications
   - Quality control mechanisms

3. **Model Development Framework**
   - Architecture selection and training
   - Model optimization strategies
   - Performance evaluation pipeline

4. **Evaluation Infrastructure**
   - Metrics selection and validation
   - Performance analysis system
   - Results visualization framework

5. **Computing Environment Architecture**
   - Resource allocation and scaling
   - HPC/GPU utilization strategy
   - Cloud storage integration

6. **Reproducibility Framework**
   - Version control and environment management
   - Experiment tracking system
   - Documentation standards

## Implementation Considerations
The proposal includes high-level specifications for:
- Recommended technology stack
- System integration points
- Resource requirements
- Core pipeline components
- Learning resources through case study implementation and framework selection

### Pipeline Components
After several iterations of development, the workflow has been refined to include these core components:
- **Video Frame Extractor** (HPC batch processing for video to frame conversion)
- **Annotation Pipeline Manager** (Workflow orchestration for labeling tasks)
- **Model Training Scheduler** (GPU resource allocation and job management)
- **Performance Evaluator** (Metrics computation and result aggregation)
- **Data Pipeline Monitor** (Processing status and resource utilization tracker)

*Note: These components are required deliverables and will be implemented as part of the system design.*

## Reproducibility Framework
### Environment Setup

This project uses a Conda environment to manage dependencies for reproducible analysis. Follow these steps to set up the environment:

#### Prerequisites
- Anaconda or Miniconda installed on your system
- Git for cloning the repository

#### Setup Instructions

1. Clone the repository and switch to the feature branch:
   ```bash
   git clone https://github.com/iTrauco/data-science-sad.git
   cd data-science-sad
   git checkout traffic-vision/multi-object-tracking
   ```

2. Create the Conda environment:
   ```bash
   conda create -n traffic-vision python=3.11 -y
   ```

3. Activate the environment:
   ```bash
   conda activate traffic-vision
   ```

4. Install baseline packages:
   ```bash
   conda install -c conda-forge jupyter numpy pandas matplotlib seaborn scikit-learn opencv -y
   ```

5. Install deep learning and computer vision packages:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install ultralytics supervision
   ```

6. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

7. Access the notebook in your browser via the URL displayed in the terminal

#### Environment Details

The environment includes essential data science and computer vision packages:
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [Jupyter Notebook](https://jupyter.org/documentation)
- [pandas](https://pandas.pydata.org/docs/) & [numpy](https://numpy.org/doc/stable/) for data manipulation
- [matplotlib](https://matplotlib.org/stable/index.html) & [seaborn](https://seaborn.pydata.org/) for visualization
- [scikit-learn](https://scikit-learn.org/stable/documentation.html) for traditional ML algorithms
- [OpenCV](https://docs.opencv.org/4.x/) for image and video processing
- [PyTorch](https://pytorch.org/docs/stable/index.html) for deep learning model development
- [Ultralytics](https://docs.ultralytics.com/) for YOLO object detection
- [Supervision](https://supervision.roboflow.com/) for object tracking utilities

#### Environment Management

For collaborators who enhance the environment with additional packages:

```bash
# Export the updated environment
conda activate traffic-vision
conda env export > environment.yml
```

This notebook serves as a comprehensive system design proposal, providing the transportation research team with a structured approach to implementing computer vision models for their multi-object tracking and video analysis task. and result aggregation)
