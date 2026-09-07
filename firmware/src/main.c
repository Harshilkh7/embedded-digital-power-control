#include "drivers.h"
#include "control.h"

int main(void) {
    board_init();
    uart_puts("Embedded Power Control FW\r\n");
    while(1) {
        /* PA1 senses the simulated 0-3.3 V feedback signal. */
        float v=((float)adc_read()/4095.0f)*3.3f;
        float duty=control_update(3.3f,v);
        pwm_set(duty);
        led_toggle();
        for(volatile unsigned long d=0; d<100000; ++d){}
    }
}
