#include <Arduino.h>
#include "drivers.h"
#include "control.h"
#include "protection.h"

namespace {
constexpr float VREF = 3.30f;
constexpr uint32_t CONTROL_PERIOD_US = 1000U; // 1 kHz
constexpr uint32_t TELEMETRY_PERIOD_MS = 100U;
uint32_t last_telemetry_ms = 0;
}

void setup() {
    board_init();
    control_reset();
    uart_puts("ESP32 Embedded Digital Power Control FW\r\n");
}

void loop() {
    const uint16_t voltage_raw = adc_read_voltage_raw();
    const uint16_t current_raw = adc_read_current_raw();
    const float voltage = adc_voltage_from_raw(voltage_raw);
    const float current = adc_current_from_raw(current_raw);
    const ProtectionState state = protection_evaluate(voltage, current);

    float duty = 0.0f;
    if (state != ProtectionState::OVERVOLTAGE &&
        state != ProtectionState::OVERCURRENT) {
        duty = control_update(VREF, voltage);
    }
    pwm_set(duty);

    const uint32_t now_ms = millis();
    if (now_ms - last_telemetry_ms >= TELEMETRY_PERIOD_MS) {
        last_telemetry_ms = now_ms;
        Serial.printf("V=%.3f,I=%.3f,D=%.3f,STATE=%s\r\n",
                      voltage, current, duty, protection_name(state));
        led_toggle();
    }

    delayMicroseconds(CONTROL_PERIOD_US);
}
