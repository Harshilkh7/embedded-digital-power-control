"""Small deterministic MCU/firmware behavior model used by validation tests."""
from dataclasses import dataclass

@dataclass
class FirmwareDevice:
    vout: float = 0.0
    state: str = "STARTUP"
    pwm_duty: float = 0.0

    def apply_measurement(self, voltage: float, current: float = 0.5) -> str:
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
        self.pwm_duty = max(0.0, min(0.95, duty))
        return self.pwm_duty
