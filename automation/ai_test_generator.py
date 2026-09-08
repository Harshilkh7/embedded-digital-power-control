from dataclasses import dataclass
import os


@dataclass(frozen=True)
class TestSpec:
    name: str
    stimulus: str
    expected: str


def _deterministic_tests(requirement: str):
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
            "Enter UNDERVOLTAGE and continue recovery control.",
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


def generate_tests(requirement: str):
    """Generate candidate validation scenarios from an engineering requirement.

    If explicitly enabled, the optional LLM adapter is used. Otherwise the
    deterministic catalog provides a reproducible offline fallback for CI.
    """
    requirement = requirement.strip()
    if not requirement:
        raise ValueError("engineering requirement must not be empty")

    if os.getenv("GENAI_TEST_GENERATOR") == "1":
        try:
            from automation.llm_test_generator import generate_tests_with_llm
            generated = generate_tests_with_llm(requirement)
            if generated:
                return generated
        except Exception:
            # Validation must remain available even when the external model is
            # unavailable, misconfigured, or returns an invalid response.
            pass

    return _deterministic_tests(requirement)
