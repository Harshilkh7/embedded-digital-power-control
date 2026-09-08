#include <Arduino.h>
#include "control.h"

namespace {
float integral = 0.0f;
constexpr float KP = 0.08f;
constexpr float KI = 80.0f;
constexpr float CONTROL_DT_S = 0.001f; // 1 kHz control loop
constexpr float MIN_OUTPUT = 0.0f;
constexpr float MAX_OUTPUT = 0.95f;
}

void control_reset(void) {
    integral = 0.0f;
}

float control_update(float reference, float measurement) {
    const float error = reference - measurement;
    const float candidate = integral + KI * error * CONTROL_DT_S;
    const float raw = KP * error + candidate;
    const float output = constrain(raw, MIN_OUTPUT, MAX_OUTPUT);

    // Conditional integration prevents the integral term from growing while
    // the actuator is saturated in the direction of the error.
    const bool high_windup = raw > MAX_OUTPUT && error > 0.0f;
    const bool low_windup = raw < MIN_OUTPUT && error < 0.0f;
    if (!high_windup && !low_windup) {
        integral = candidate;
    }
    return output;
}
