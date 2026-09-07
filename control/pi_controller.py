from dataclasses import dataclass

@dataclass
class PIController:
    kp: float
    ki: float
    dt: float
    minimum: float = 0.0
    maximum: float = 0.95
    integral: float = 0.0

    def reset(self):
        self.integral = 0.0

    def update(self, reference, measurement):
        error = reference - measurement
        candidate = self.integral + self.ki * error * self.dt
        raw = self.kp * error + candidate
        output = max(self.minimum, min(self.maximum, raw))
        high_windup = raw > self.maximum and error > 0
        low_windup = raw < self.minimum and error < 0
        if not (high_windup or low_windup):
            self.integral = candidate
        return output
