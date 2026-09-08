#include <Arduino.h>
#include "drivers.h"
#include "control.h"

int main(void) {
    initArduino();
    board_init();
    uart_puts("ESP32 Embedded Digital Power Control FW\r\n");

    while (true) {
        const float voltage = (static_cast<float>(adc_read()) / 4095.0f) * 3.3f;
        const float duty = control_update(3.3f, voltage);
        pwm_set(duty);
        led_toggle();
        delay(10);
    }
}

extern "C" void app_main(void) {
    main();
}
