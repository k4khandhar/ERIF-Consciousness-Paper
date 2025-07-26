# ERIF Theory: A Cognitive Map for Consciousness

[![ERIF Map](docs/visuals/erif_map.png)](https://k4khandhar.github.io/ERIF-Consciousness-Paper)

## Overview
ERIF is a 2D cognitive map modeling consciousness as a dynamic journey across Stability (T) and Integration (R). It applies to human brains, AI systems, and beyond. This repo contains the theory paper, simulations, and an open-source toolkit.

- **Key Idea**: Consciousness isn't static—it's movement through cognitive space.
- **Built With**: NetLogo, Python, Colab, Plotly.
- **Links**: [Website](https://k4khandhar.github.io/ERIF-Consciousness-Paper) | [Google Drive](https://drive.google.com/drive/folders/1wJ_mvKZ1XBofNy7sPolynPEtUgWwMu9-) | [Medium Post](https://medium.com/... )  <!-- Add your published link -->

## ERIF Theory Summary
ERIF models consciousness as paths in a 2D space:
- **T (Stability)**: Drive for consistency and grounding.
- **R (Integration)**: Drive for growth and adaptation.
Math: dT/dt = α(success - entropy); dR/dt = β(info_gain - overload).
Applications: Evolution from cells to AI, EEG state mapping, agent simulations.

For full details, see [docs/ERIF_Theory_v1.0.pdf](docs/ERIF_Theory_v1.0.pdf).

## Key Files and Folders
- **/docs/**: Theory papers and visuals.
  - ERIF_Theory_v1.0.pdf: Main paper with math, sims, EEG.
- **/lab-suite/core/**: Toolkit code.
  - erif_colab_suite.ipynb: Main demo (sims, plots).
  - erif_eeg_visualizer.ipynb: EEG mapping and visualization.
  - erif_main_sim.py: Core simulation runner.
  - erif_plotly_dashboard.py: Real-time T/R dashboard.
  - erif_python_netlogo_bridge.py: NetLogo integration.
- **/notebooks/**: Prototypes.
  - ERIF_AGI_Wrapper_Prototype.ipynb: AGI extensions.
- **/research/**: Important data and outputs (sim results, EEG studies, final experiments).
  - /research/simulations/: NetLogo results (CSV, plots, logs).
  - /research/meditation/: EEG data from meditation studies (CSV, PDF, plots).
  - /research/final_study/: Culminating study outputs (CSV, PDF, plots).
  - Other moved data: From project outputs, experiments (CSV, PNG, etc.).

## Quick Start
1. Clone the repo: `git clone https://github.com/k4khandhar/ERIF-Consciousness-Paper.git`
2. Run the Colab toolkit: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/k4khandhar/ERIF-Consciousness-Paper/blob/main/lab-suite/core/erif_colab_suite.ipynb)
3. Explore simulations: Open /lab-suite/core/erif_main_sim.py or NetLogo models in /research/simulations/.

## Installation
- Requirements: Python 3.x, NetLogo, Jupyter/Colab.
- Install: `pip install -r requirements.txt`

## Usage
- Simulate: Run erif_main_sim.py for T/R paths.
- Visualize EEG: Open erif_eeg_visualizer.ipynb.
- See research data: Check /research/ for CSV/plots from studies.

## Theory Highlights
- Math and comparisons in the paper.
- Data from real studies in /research/.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). Fork, create issues, or PRs welcome!

## License
MIT License—see [LICENSE](LICENSE).

## Contact
Rohit Khandhar · [@k4khandhar](https://twitter.com/k4khandhar) · Issues welcome!
