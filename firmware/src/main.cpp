#include <Arduino.h>
#include "drivers.h"
#include "control.h"

void setup() {
    board_init();
    control_reset();
    uart_puts("ESP32 Embedded Digital Power Control FW\r\n");
}

void loop() {
    const float voltage = (static_cast<float>(adc_read()) / 4095.0f) * 3.3f;
    const float duty = control_update(3.3f, voltage);
    pwm_set(duty);
    led_toggle();
    delay(10);
}
