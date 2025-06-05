# AI, ML, Data Science, and Research Systems Analysis and Design (SAD)

This repository contains case studies, each scoped to their own branch, that demonstrate systems analysis and design approaches to the challenges of AI, ML, data science, and scientific research computing.

Each case study applies a comprehensive problem-solving methodology that views system design as 'a search or problem-solving process that uses means to achieve desired ends' ([Strohmann et al., 2023](https://lutpub.lut.fi/bitstream/handle/10024/166324/strohmann_et_al_design_principles_publishers_version.pdf?sequence=3&isAllowed=y)). This holistic approach integrates multiple types of knowledge from understanding the problem domain to developing practical solutions, creating a framework that addresses the complex, interconnected challenges found in modern computational research environments.

The methodology's strength lies in its proven versatility across diverse technical domains, making it particularly effective for the multifaceted challenges of research computing infrastructure.

## Purpose

This repository demonstrates technical approaches to designing and implementing AI, ML, data science, and scientific computational systems that balance performance, scalability, and usability. It highlights architectural considerations for diverse computational and research workflows.

## Structure

The repository uses a branch-based organization where each case study is self-contained:

- `main`: Contains the overview README and repository documentation
- Case study branches: Each scenario is developed in its own dedicated branch with:
  - Individual README with scenario-specific documentation
  - `.gitignore` for environment-specific exclusions
  - `notebooks/` directory containing the proposal Jupyter notebook
  - `components/` directory with implementation modules, each in their own subdirectory
  - `environment.yml` containing all conda environment specifications for the case study and its components

## Case Studies Overview

| Scenario | Topic | Notebook | Status |
|:--------:|-------|:--------:|:------:|
| 1 | [Imbalanced Classification System Design](https://github.com/iTrauco/data-science-sad/tree/feature/scenario1-imbalanced-classification) | [Case Study Proposal Notebook](https://github.com/iTrauco/data-science-sad/blob/feature/scenario1-imbalanced-classification/notebooks/Imbalanced_Classification_Deep_Learning_System_Analysis_And_Design_Proposal.ipynb) | 🔒 |
| 2 | [Microscopy Classification](https://github.com/iTrauco/data-science-sad/tree/feature/scenario2-microscopy-classification) | [Case Study Proposal Notebook](https://github.com/iTrauco/data-science-sad/blob/feature/scenario2-microscopy-classification/notebooks/Microscopy_Image_Classification_Deep_Learning_System_Analysis_And_Design_Proposal.ipynb) | 🔒 |
| 3 | [Ocean Sensors Concept Drift](https://github.com/iTrauco/data-science-sad/tree/scenario3-ocean-sensors/concept-drift) | TBD | ⚫ |
| 4 | [Seismic Monitoring Extreme Imbalance](https://github.com/iTrauco/data-science-sad/tree/scenario4-seismic-monitoring/extreme-imbalance) | TBD | ⚫ |
| 5 | [Climate Science Multimodal Fusion](https://github.com/iTrauco/data-science-sad/tree/scenario5-climate-science/multimodal-fusion) | TBD | ⚫ |
| 6 | [Traffic Vision Multi-Object Tracking](https://github.com/iTrauco/data-science-sad/tree/scenario06/traffic-vision/multi-object-tracking) | [Case Study Proposal Notebook](https://github.com/iTrauco/data-science-sad/blob/scenario06/traffic-vision/multi-object-tracking/notebooks/%5BDRAFT%5DTraffic%20Vision%20Multi-Object%20Tracking%20-%20System%20Analysis%20and%20Design%20Proposal.ipynb) | 🟡 |
| 7 | [Lab ISO17025 3D Scanner Validation](https://github.com/iTrauco/data-science-sad/tree/scenario07/lab-iso17025/3d-scanner-validation) | TBD | ⚫ |
| 8 | [3D Scan Format Conversion](https://github.com/iTrauco/data-science-sad/tree/scenario08/3d-scan/format-conversion) | TBD | ⚫ |
| 9 |  |  |  |
| 10 |  |  |  |
| 11 |  |  |  |
| 12 |  |  |  |
| 13 |  |  |  |
| 14 |  |  |  |
| 15 |  |  |  |
| 16 |  |  |  |
| 17 |  |  |  |
| 18 |  |  |  |
| 19 |  |  |  |
| 20 |  |  |  |

**Status Key:** ⚫ Not Started | 🟡 In Progress | 🟢 Complete | 🔒 On Hold | 🔴 Abandoned