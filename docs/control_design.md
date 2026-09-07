# Control Design

The digital controller implements:

e[k] = Vref - Vout[k]

I[k] = I[k-1] + Ki * e[k] * Ts

D[k] = Kp * e[k] + I[k]

The duty command is saturated to 0...0.95. Conditional anti-windup prevents
the integrator from accumulating when the output is already saturated in the
same direction as the error.

The buck model is an averaged differential-equation model, suitable for
controller development and regression testing rather than transistor-level
SPICE analysis.
