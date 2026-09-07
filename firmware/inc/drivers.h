#ifndef DRIVERS_H
#define DRIVERS_H
#include <stdint.h>
void gpio_init(void); void led_toggle(void);
void pwm_init(void); void pwm_set(float duty);
void uart_init(void); void uart_puts(const char*);
void spi_init(void); uint8_t spi_transfer(uint8_t);
void i2c_init(void);
void adc_init(void); uint16_t adc_read(void);
#endif
