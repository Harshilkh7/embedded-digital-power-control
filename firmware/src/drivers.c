#include "stm32f103.h"
#include "drivers.h"

static void clock_init(void) {
    /* HSE 8 MHz -> PLL x9 -> 72 MHz SYSCLK. APB1 = 36 MHz, APB2 = 72 MHz. */
    RCC->CR |= 1U << 16;
    while (!(RCC->CR & (1U << 17))) {}
    FLASH_ACR = (1U << 4) | 2U; /* Prefetch + 2 wait states. */
    RCC->CFGR = (RCC->CFGR & ~((0xFU << 4) | (7U << 8) | (7U << 11) | (1U << 16) | (1U << 17) | (0xFU << 18)))
              | (4U << 8) | (4U << 18) | (1U << 16); /* APB1 /2, PLL source HSE, x9. */
    RCC->CR |= 1U << 24;
    while (!(RCC->CR & (1U << 25))) {}
    RCC->CFGR = (RCC->CFGR & ~3U) | 2U;
    while (((RCC->CFGR >> 2) & 3U) != 2U) {}
}

void gpio_init(void) {
    RCC->APB2ENR |= 1U<<4;
    GPIOC->CRH = (GPIOC->CRH & ~(0xFU<<20)) | (0x2U<<20);
}
void led_toggle(void) { GPIOC->ODR ^= 1U<<13; }

void pwm_init(void) {
    RCC->APB2ENR |= 1U<<2; RCC->APB1ENR |= 1U;
    /* PA0 = TIM2_CH1 PWM output. */
    GPIOA->CRL = (GPIOA->CRL & ~0xFU) | 0xBU;
    TIM2->PSC=0; TIM2->ARR=3599; TIM2->CCR1=0;
    TIM2->CCMR1=(6U<<4)|(1U<<3); TIM2->CCER=1; TIM2->EGR=1; TIM2->CR1=1;
}
void pwm_set(float duty) {
    if(duty<0)duty=0; if(duty>.95f)duty=.95f;
    TIM2->CCR1=(uint32_t)(duty*TIM2->ARR);
}

void uart_init(void) {
    RCC->APB2ENR |= (1U<<2)|(1U<<14);
    GPIOA->CRH=(GPIOA->CRH&~((0xFU<<4)|(0xFU<<8)))|(0xBU<<4)|(0x4U<<8);
    /* USART1 on 72 MHz APB2, 115200 baud. */
    USART1->BRR=0x271; USART1->CR1=(1U<<13)|(1U<<3)|(1U<<2);
}
void uart_puts(const char*s) { while(*s){while(!(USART1->SR&(1U<<7))){} USART1->DR=*s++;} }

void spi_init(void) {
    RCC->APB2ENR |= (1U<<2)|(1U<<12);
    GPIOA->CRL=(GPIOA->CRL&~((0xFU<<20)|(0xFU<<24)|(0xFU<<28)))|
               (0xBU<<20)|(0x4U<<24)|(0xBU<<28);
    SPI1->CR1=(1U<<2)|(1U<<9)|(1U<<8)|(2U<<3)|(1U<<6);
}
uint8_t spi_transfer(uint8_t d) {
    while(!(SPI1->SR&(1U<<1))){} SPI1->DR=d;
    while(!(SPI1->SR&1U)){} return (uint8_t)SPI1->DR;
}

void i2c_init(void) {
    RCC->APB2ENR|=1U<<3; RCC->APB1ENR|=1U<<21;
    GPIOB->CRL=(GPIOB->CRL&~((0xFU<<24)|(0xFU<<28)))|(0xFU<<24)|(0xFU<<28);
    /* PCLK1 = 36 MHz -> standard-mode 100 kHz. */
    I2C1->CR2=36; I2C1->CCR=180; I2C1->TRISE=37; I2C1->CR1=1;
}

void adc_init(void) {
    RCC->APB2ENR|=1U<<2; /* GPIOA */
    RCC->APB2ENR|=1U<<9; /* ADC1 */
    /* PA1 = ADC1_IN1 analog feedback input; PA0 remains PWM. */
    GPIOA->CRL &= ~(0xFU << 4);
    ADC1->CR2=1; ADC1->SMPR2=7; ADC1->SQR1=0; ADC1->SQR3=1;
    ADC1->CR2|=1U<<2; while(ADC1->CR2&(1U<<2)){}
}
uint16_t adc_read(void) {
    ADC1->CR2|=1U<<22; while(!(ADC1->SR&(1U<<1))){} return (uint16_t)ADC1->DR;
}

void board_init(void) {
    clock_init();
    gpio_init(); pwm_init(); uart_init(); spi_init(); i2c_init(); adc_init();
}
