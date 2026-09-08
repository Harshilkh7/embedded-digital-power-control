from dataclasses import dataclass


@dataclass(frozen=True)
class TestSpec:
    name: str
    stimulus: str
    expected: str


def generate_tests(requirement: str):
    """Generate candidate validation scenarios from an engineering requirement.

    The deterministic catalog is the safe offline fallback. A production LLM
    adapter can return the same TestSpec contract without changing the runner.
    """
    requirement = requirement.strip()
    if not requirement:
        raise ValueError("engineering requirement must not be empty")

    return [
        TestSpec(
            "nominal_regulation",
            "Set Vin=5 V and Vref=3.3 V on the ESP32-controlled buck stage.",
            "Vout remains inside the 3.3 V regulation tolerance.",
        ),
        TestSpec(
            "load_step",
            "Decrease load resistance during closed-loop regulation.",
            "Vout returns to the regulation band after the load step.",
        ),
        TestSpec(
            "over_voltage",
            "Force sensed voltage above 3.63 V.",
            "Enter OVERVOLTAGE and command zero PWM.",
        ),
        TestSpec(
            "under_voltage",
            "Force sensed voltage below 2.80 V.",
            "Enter UNDERVOLTAGE and command zero PWM.",
        ),
        TestSpec(
            "over_current",
            "Force sensed current above 2.00 A while voltage is nominal.",
            "Enter OVERCURRENT and command zero PWM.",
        ),
        TestSpec(
            "pwm_bounds",
            "Request PWM values below 0% and above 95%.",
            "Clamp commands to the safe 0..95% range.",
        ),
    ]
