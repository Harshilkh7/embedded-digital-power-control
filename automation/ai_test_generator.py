from dataclasses import dataclass


@dataclass
class TestSpec:
    name: str
    stimulus: str
    expected: str


def generate_tests(requirement):
    """Generate candidate validation scenarios for the ESP32 power controller.

    This deterministic implementation is the GenAI integration boundary. An
    approved LLM API can replace this function without changing the runner.
    """
    return [
        TestSpec(
            "nominal_regulation",
            "Set Vin=5 V and Vref=3.3 V on the ESP32-controlled buck stage.",
            "Vout converges to 3.3 V within tolerance.",
        ),
        TestSpec(
            "load_step",
            "Decrease load resistance during ESP32 closed-loop regulation.",
            "Vout returns to the regulation band.",
        ),
        TestSpec(
            "over_voltage",
            "Force the ESP32 sensed voltage above the 3.63 V protection threshold.",
            "Protection enters OVERVOLTAGE and disables PWM.",
        ),
    ]
