def print_audit_report(n_bottles, actual_mean, target, upper_limit, overfill_count, rate, loss):
    """
    Prints a formatted diagnostic report to the console.
    """
    print(f"\n--- CALIBRATION AUDIT REPORT ---")
    print(f"Total Bottles Analyzed: {n_bottles}")
    print(f"Observed Average:      {actual_mean:.2f} ml")
    print(f"Target Deviation (Bias): {actual_mean - target:.2f} ml")
    print("-" * 40)
    print(f"Upper Limit Threshold:  {upper_limit} ml")
    print(f"Out-of-Range Bottles:   {overfill_count}")
    print(f"Overfill Rate:          {rate:.2f}%")
    print(f"Estimated Economic Loss: ${loss:.2f} USD")
    print("-" * 40)