"""Reusable fault stimuli for embedded validation."""
def faults():
    return [
        {"name": "over_voltage", "voltage": 3.8, "current": 0.5, "expected": "OVERVOLTAGE"},
        {"name": "under_voltage", "voltage": 2.5, "current": 0.5, "expected": "UNDERVOLTAGE"},
        {"name": "over_current", "voltage": 3.3, "current": 2.5, "expected": "OVERCURRENT"},
    ]
