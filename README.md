# Imbalanced Classification System Design Proposal

## Scenario Overview
A researcher is working on a classification task with an imbalanced dataset (~1M rows, 30 features, 3% positive class). They want to use deep learning but are unsure where to start. This proposal outlines a systems approach for model development, data handling, and evaluation—including infrastructure recommendations for scalability and reproducibility.

## Proposal Framework
This Jupyter notebook presents a systems analysis and design approach to the imbalanced classification challenge. The proposal follows established information systems design principles, emphasizing:
- **Systematic Analysis**: Methodical breakdown of requirements and constraints
- **Architectural Planning**: Structured approach to system components and their interactions
- **Implementation Roadmap**: Process-oriented development strategy
- **Evaluation Framework**: Comprehensive assessment methodology

## System Components
The proposed solution addresses the following key subsystems:
1. **Data Processing Subsystem**
   - Data flow architecture
   - Imbalance handling mechanisms
   - Pre-processing pipeline design
2. **Model Development Framework**
   - Architecture selection methodology
   - Training system design
   - Parameter optimization approach
3. **Evaluation Infrastructure**
   - Metrics selection framework
   - Validation process design
   - Performance analysis system
4. **Computing Environment Architecture**
   - Resource allocation strategy
   - Scaling methodology
   - System integration approach
5. **Reproducibility Framework**
   - Version control strategy
   - Environment specification
   - Documentation system

## Implementation Considerations
The proposal includes high-level specifications for:
- Recommended technology stack
- System integration points
- Resource requirements
- Timeline and milestones
- Knowledge transfer methodology

## Reproducibility Framework
### Environment Setup

This project uses a Conda environment to manage dependencies for reproducible analysis. Follow these steps to set up the environment:

#### Prerequisites
- Anaconda or Miniconda installed on your system
- Git for cloning the repository

#### Setup Instructions

1. Clone the repository and switch to the feature branch:
   ```bash
   git clone https://github.com/iTrauco/ai-data-science-sad.git
   cd ai-data-science-sad
   git checkout feature/scenario1-imbalanced-classification
   ```

2. Create the Conda environment from the environment file:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate scenario01
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Access the notebook in your browser via the URL displayed in the terminal

#### Environment Details

The environment includes essential data science packages:
- Python 3.11
- Jupyter Notebook
- pandas & numpy for data manipulation
- matplotlib, seaborn & plotly for visualization
- scikit-learn for traditional ML algorithms
- Deep learning frameworks for model development

#### Environment Management

For collaborators who enhance the environment with additional packages:

```bash
# Export the updated environment
conda activate scenario01
conda env export > environment.yml
```

This notebook serves as a comprehensive system design proposal, providing the researcher with a structured approach to implementing deep learning for their imbalanced classification task.

> **Note**: All work for this project is scoped to the `feature/scenario1-imbalanced-classification` branch only.