from dataclasses import dataclass
import numpy as np

@dataclass
class BuckConverter:
    vin: float = 5.0
    inductance: float = 10e-6
    capacitance: float = 100e-6
    load_resistance: float = 2.0
    vout: float = 0.0
    current: float = 0.0

    def step(self, duty, dt):
        duty = float(np.clip(duty, 0.0, 0.95))
        di = (duty * self.vin - self.vout) / self.inductance
        dv = (self.current - self.vout / self.load_resistance) / self.capacitance
        self.current = max(0.0, self.current + di * dt)
        self.vout = max(0.0, self.vout + dv * dt)
        return self.vout

def simulate(reference=3.3, total_time=0.02, dt=1e-6,
             controller=None, plant=None, load_step=None):
    from .pi_controller import PIController
    controller = controller or PIController(.08, 80.0, dt)
    plant = plant or BuckConverter()
    n = int(total_time / dt)
    t = np.arange(n) * dt
    v = np.zeros(n); d = np.zeros(n); i = np.zeros(n)
    for k, now in enumerate(t):
        if load_step and now >= load_step[0]:
            plant.load_resistance = load_step[1]
        d[k] = controller.update(reference, plant.vout)
        v[k] = plant.step(d[k], dt)
        i[k] = plant.current
    return t, v, d, i

def metrics(t, v, reference, tolerance=0.02):
    final = float(v[-1]); peak = float(v.max())
    outside = np.where(np.abs(v-reference) > tolerance*abs(reference))[0]
    settling = float(t[-1]) if len(outside) == 0 else float(t[min(outside[-1]+1, len(t)-1)])
    return {"final_voltage": final, "steady_state_error": abs(reference-final), "overshoot_percent": max(0.0, (peak-reference)/reference*100), "settling_time_s": settling}
