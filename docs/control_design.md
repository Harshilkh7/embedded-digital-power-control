# Control Design

The digital controller implements a discrete PI regulator:

```text
e[k] = Vref - Vout[k]
I[k] = I[k-1] + Ki * e[k] * Ts
D[k] = Kp * e[k] + I[k]
```

The duty command is saturated to `0...0.95`. Conditional anti-windup prevents
integrator accumulation when the actuator is saturated in the same direction
as the error.

## Embedded controller

- `Kp = 0.08`
- `Ki = 80.0`
- `Ts = 1 ms` (1 kHz control update)
- PWM frequency = 20 kHz
- PWM resolution = 12 bits
- Duty limit = 95%

The firmware reads ADC voltage feedback, computes the PI command and updates
the ESP32 LEDC PWM peripheral. Over-voltage and over-current protection force
zero duty; under-voltage is reported as a regulation fault while the
controller continues attempting recovery.

## Plant model

The Python buck model uses averaged inductor-current and capacitor-voltage
differential equations. It is intended for controller development and
regression testing rather than transistor-level SPICE analysis.

For a nominal 5 V input and 3.3 V target, the ideal steady-state buck relation
is approximately `Vout = D * Vin`, giving a nominal duty near 66%. The PI
controller then compensates for load and model dynamics.
