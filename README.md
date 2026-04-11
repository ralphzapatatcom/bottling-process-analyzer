# Bottling Process Optimization Lab 🍾

An automated diagnostic tool designed to detect calibration drift in liquid bottling lines. This project simulates real-world production data, identifies overfill inefficiencies, and calculates the resulting economic impact.

## 📌 Project Overview

In industrial bottling, "invisible" calibration errors can lead to significant financial losses. This tool identifies when a machine is overfilling beyond technical tolerances, even when the control panel might suggest everything is normal.

### Key Features
* **Calibration Bias Detection:** Calculates the gap between target volume and actual output.
* **Quality Audit Reporting:** Automatically generates a diagnostic summary of the production run.
* **Financial Impact Analysis:** Estimates the USD loss caused by overfilling.
* **Sensor Adjustment Logs:** Exports critical data points for maintenance teams to recalibrate hardware.

## 📂 Project Structure

* `analyze.py`: Core logic for quality metrics and financial calculations.
* `visualize.py`: Formatting engine for the audit reports.
* `config.json`: Centralized parameters (target volumes, costs, and bias settings).
* `__main__.py`: Main execution script that orchestrates the simulation.
* `requirements.txt`: List of necessary Python dependencies.

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* NumPy

### Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt