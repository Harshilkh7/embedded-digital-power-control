#ifndef DRIVERS_H
#define DRIVERS_H
#include <stdint.h>

void board_init(void);
void gpio_init(void);
void led_toggle(void);
void pwm_init(void);
void pwm_set(float duty);
void uart_init(void);
void uart_puts(const char *s);
void spi_init(void);
uint8_t spi_transfer(uint8_t data);
void i2c_init(void);
void adc_init(void);
uint16_t adc_read_voltage_raw(void);
uint16_t adc_read_current_raw(void);
float adc_voltage_from_raw(uint16_t raw);
float adc_current_from_raw(uint16_t raw);

#endif
