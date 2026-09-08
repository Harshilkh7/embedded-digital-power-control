"""Deterministic ESP32 firmware behavior model used by validation tests.

This model represents the externally observable behavior of the ESP32
power-control firmware so the validation framework can run without physical
hardware or an API key.
"""
from dataclasses import dataclass


@dataclass
class FirmwareDevice:
    """Minimal ESP32 power-control device model for automated validation."""

    target: str = "ESP32 DevKit"
    vout: float = 0.0
    state: str = "STARTUP"
    pwm_duty: float = 0.0

    def apply_measurement(self, voltage: float, current: float = 0.5) -> str:
        """Apply sensed power-stage values and evaluate protection state."""
        if voltage > 3.63:
            self.state = "OVERVOLTAGE"
            self.pwm_duty = 0.0
        elif voltage < 2.80:
            self.state = "UNDERVOLTAGE"
        elif current > 2.0:
            self.state = "OVERCURRENT"
            self.pwm_duty = 0.0
        else:
            self.state = "REGULATING"
        self.vout = voltage
        return self.state

    def set_pwm(self, duty: float) -> float:
        """Apply the validated 0..95% PWM command range."""
        self.pwm_duty = max(0.0, min(0.95, duty))
        return self.pwm_duty
