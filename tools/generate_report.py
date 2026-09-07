from pathlib import Path
import matplotlib.pyplot as plt
from control.buck_model import simulate, metrics

Path("artifacts").mkdir(exist_ok=True)
t, v, duty, current = simulate()
m = metrics(t, v, 3.3)

fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot(111)
ax.plot(t*1000, v, label="Vout")
ax.axhline(3.3, linestyle="--", label="Reference")
ax.set(xlabel="Time [ms]", ylabel="Voltage [V]", title="Closed-Loop Buck Converter Response")
ax.grid(True); ax.legend(); fig.tight_layout()
fig.savefig("artifacts/control_response.png", dpi=160)
plt.close(fig)

report = "\n".join([
    "Embedded Power Control Validation Report",
    "========================================",
    f"Final voltage: {m['final_voltage']:.4f} V",
    f"Steady-state error: {m['steady_state_error']:.4f} V",
    f"Overshoot: {m['overshoot_percent']:.2f} %",
    f"Settling time: {m['settling_time_s']*1000:.3f} ms",
    f"Final duty: {duty[-1]:.4f}",
    f"Peak inductor current: {current.max():.4f} A",
])
Path("artifacts/validation_report.txt").write_text(report)
print(report)
