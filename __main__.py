import numpy as np
import json
from analyze import calculate_quality_metrics
from visualize import print_audit_report

# 1. Load Configuration
with open('config.json') as f:
    config = json.load(f)

# 2. Simulation Setup
np.random.seed(42)
real_mean = config['target_volume'] + config['calibration_bias']

# Generate Real-world Data [ID, Volume, Temperature]
raw_data = np.zeros((config['sample_size'], 3))
raw_data[:, 0] = np.arange(config['sample_size'])
raw_data[:, 1] = np.random.normal(real_mean, config['std_deviation'], config['sample_size'])
raw_data[:, 2] = np.random.normal(15, 0.5, config['sample_size'])

# 3. Data Analysis
results = calculate_quality_metrics(
    raw_data, 
    config['target_volume'], 
    config['std_deviation'], 
    config['cost_per_ml']
)

# 4. Reporting & Export
print_audit_report(
    config['sample_size'],
    np.mean(raw_data[:, 1]),
    config['target_volume'],
    results['upper_limit'],
    len(results['overfilled_data']),
    results['overfill_rate'],
    results['financial_loss']
)

# Export critical cases for sensor recalibration
np.savetxt(
    "sensor_adjustment_log.csv", 
    results['overfilled_data'], 
    delimiter=",", 
    header="ID,Actual_Volume,Temp", 
    comments=''
)