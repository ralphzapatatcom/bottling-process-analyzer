import numpy as np

def calculate_quality_metrics(data, target, std_dev, cost_unit):
    """
    Analyzes the real data against the ideal technical specifications.
    """
    upper_limit = target + (2 * std_dev)
    lower_limit = target - (2 * std_dev)
    
    # Identify overfilled bottles (Economic loss)
    overfilled_mask = data[:, 1] > upper_limit
    overfilled_bottles = data[overfilled_mask]
    
    overfill_rate = (len(overfilled_bottles) / len(data)) * 100
    
    # Calculate financial impact
    excess_ml = np.sum(overfilled_bottles[:, 1] - target)
    estimated_loss = excess_ml * cost_unit
    
    return {
        "overfilled_data": overfilled_bottles,
        "overfill_rate": overfill_rate,
        "financial_loss": estimated_loss,
        "upper_limit": upper_limit,
        "lower_limit": lower_limit
    }