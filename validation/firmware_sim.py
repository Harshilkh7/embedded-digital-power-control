"""Deterministic model of externally observable ESP32 firmware behavior."""
from dataclasses import dataclass


@dataclass
class FirmwareDevice:
    """ESP32 power-controller behavior model used by automated validation."""

    target: str = "ESP32 DevKit"
    vout: float = 0.0
    state: str = "STARTUP"
    pwm_duty: float = 0.0

    def apply_measurement(self, voltage: float, current: float = 0.5) -> str:
        """Apply sensed values and enforce the firmware protection policy."""
        self.vout = float(voltage)
        if voltage > 3.63:
            self.state = "OVERVOLTAGE"
            self.pwm_duty = 0.0
        elif voltage < 2.80:
            # UV is treated as a regulation fault: the controller keeps
            # driving the plant so it can recover from a low output voltage.
            self.state = "UNDERVOLTAGE"
        elif current > 2.0:
            self.state = "OVERCURRENT"
            self.pwm_duty = 0.0
        elif voltage < 3.0 or voltage > 3.5 or current > 1.5:
            self.state = "WARNING"
        else:
            self.state = "REGULATING"
        return self.state

    def set_pwm(self, duty: float) -> float:
        """Apply the validated 0..95% PWM command range."""
        self.pwm_duty = max(0.0, min(0.95, float(duty)))
        return self.pwm_duty

    def reset_protection(self) -> None:
        """Return the simulated controller to a safe startup state."""
        self.state = "STARTUP"
        self.pwm_duty = 0.0
