#include <Arduino.h>
#include "control.h"

static float integral = 0.0f;

void control_reset(void) {
    integral = 0.0f;
}

float control_update(float reference, float measurement) {
    constexpr float kp = 0.08f;
    constexpr float ki = 80.0f;
    constexpr float dt = 0.01f;
    constexpr float min_output = 0.0f;
    constexpr float max_output = 0.95f;

    const float error = reference - measurement;
    const float candidate = integral + ki * error * dt;
    const float raw = kp * error + candidate;
    const float output = constrain(raw, min_output, max_output);

    const bool high_windup = raw > max_output && error > 0.0f;
    const bool low_windup = raw < min_output && error < 0.0f;
    if (!high_windup && !low_windup) {
        integral = candidate;
    }
    return output;
}
