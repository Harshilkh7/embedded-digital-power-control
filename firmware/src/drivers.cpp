#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>
#include "drivers.h"

namespace {
constexpr uint8_t LED_PIN = 2;
constexpr uint8_t PWM_PIN = 25;
constexpr uint8_t ADC_PIN = 34;
constexpr uint8_t I2C_SDA = 21;
constexpr uint8_t I2C_SCL = 22;
constexpr uint8_t SPI_SCK = 18;
constexpr uint8_t SPI_MISO = 19;
constexpr uint8_t SPI_MOSI = 23;
constexpr uint8_t SPI_CS = 5;
constexpr uint8_t PWM_CHANNEL = 0;
constexpr uint32_t PWM_FREQUENCY = 20000;
constexpr uint8_t PWM_BITS = 12;
constexpr uint16_t PWM_MAX = (1U << PWM_BITS) - 1U;
}

void gpio_init(void) {
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
}

void led_toggle(void) {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
}

void pwm_init(void) {
    // Compatible with the Arduino-ESP32 core used by the pinned PlatformIO build.
    ledcSetup(PWM_CHANNEL, PWM_FREQUENCY, PWM_BITS);
    ledcAttachPin(PWM_PIN, PWM_CHANNEL);
    ledcWrite(PWM_CHANNEL, 0);
}

void pwm_set(float duty) {
    duty = constrain(duty, 0.0f, 0.95f);
    ledcWrite(PWM_CHANNEL, static_cast<uint32_t>(duty * PWM_MAX));
}

void uart_init(void) {
    Serial.begin(115200);
}

void uart_puts(const char *s) {
    Serial.print(s);
}

void spi_init(void) {
    pinMode(SPI_CS, OUTPUT);
    digitalWrite(SPI_CS, HIGH);
    SPI.begin(SPI_SCK, SPI_MISO, SPI_MOSI, SPI_CS);
}

uint8_t spi_transfer(uint8_t data) {
    SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
    digitalWrite(SPI_CS, LOW);
    const uint8_t response = SPI.transfer(data);
    digitalWrite(SPI_CS, HIGH);
    SPI.endTransaction();
    return response;
}

void i2c_init(void) {
    Wire.begin(I2C_SDA, I2C_SCL, 100000);
}

void adc_init(void) {
    analogReadResolution(12);
    analogSetPinAttenuation(ADC_PIN, ADC_11db);
}

uint16_t adc_read(void) {
    return static_cast<uint16_t>(analogRead(ADC_PIN));
}

void board_init(void) {
    gpio_init();
    pwm_init();
    uart_init();
    spi_init();
    i2c_init();
    adc_init();
}
