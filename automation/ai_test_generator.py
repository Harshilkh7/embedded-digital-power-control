from dataclasses import dataclass

@dataclass
class TestSpec:
    name: str
    stimulus: str
    expected: str

def generate_tests(requirement):
    # Deterministic fallback; replace this boundary with an approved LLM API.
    return [
        TestSpec("nominal_regulation", "Set Vin=5 V and Vref=3.3 V.", "Vout converges to 3.3 V within tolerance."),
        TestSpec("load_step", "Decrease load resistance during regulation.", "Vout returns to the regulation band."),
        TestSpec("over_voltage", "Force sensed voltage above OVLO.", "Protection enters OVERVOLTAGE.")
    ]
