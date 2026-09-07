#ifndef STM32F103_H
#define STM32F103_H
#include <stdint.h>
#define APB2 0x40010000UL
#define APB1 0x40000000UL
#define AHB  0x40020000UL
#define RCC_BASE (AHB+0x1000)
#define FLASH_ACR_ADDR 0x40022000UL
#define GPIOA_BASE (APB2+0x800)
#define GPIOB_BASE (APB2+0xC00)
#define GPIOC_BASE (APB2+0x1000)
#define USART1_BASE (APB2+0x13800)
#define SPI1_BASE (APB2+0x13000)
#define I2C1_BASE (APB1+0x5400)
#define TIM2_BASE APB1
#define ADC1_BASE (APB2+0x12400)

typedef struct { volatile uint32_t CR,CFGR,CIR,APB2RSTR,APB1RSTR,AHBENR,APB2ENR,APB1ENR,BDCR,CSR; } RCC_t;
typedef struct { volatile uint32_t CRL,CRH,IDR,ODR,BSRR,BRR,LCKR; } GPIO_t;
typedef struct { volatile uint32_t SR,DR,BRR,CR1,CR2,CR3,GTPR; } USART_t;
typedef struct { volatile uint32_t CR1,CR2,SR,DR,CRCPR,RXCRCR,TXCRCR,I2SCFGR,I2SPR; } SPI_t;
typedef struct { volatile uint32_t CR1,CR2,OAR1,OAR2,DR,SR1,SR2,CCR,TRISE; } I2C_t;
typedef struct { volatile uint32_t CR1,CR2,SMCR,DIER,SR,EGR,CCMR1,CCMR2,CCER,CNT,PSC,ARR,RCR,CCR1,CCR2,CCR3,CCR4; } TIM_t;
typedef struct { volatile uint32_t SR,CR1,CR2,SMPR1,SMPR2,JOFR1,JOFR2,JOFR3,JOFR4,HTR,LTR,SQR1,SQR2,SQR3,JSQR,JDR1,JDR2,JDR3,JDR4,DR; } ADC_t;
#define RCC ((RCC_t*)RCC_BASE)
#define GPIOA ((GPIO_t*)GPIOA_BASE)
#define GPIOB ((GPIO_t*)GPIOB_BASE)
#define GPIOC ((GPIO_t*)GPIOC_BASE)
#define USART1 ((USART_t*)USART1_BASE)
#define SPI1 ((SPI_t*)SPI1_BASE)
#define I2C1 ((I2C_t*)I2C1_BASE)
#define TIM2 ((TIM_t*)TIM2_BASE)
#define ADC1 ((ADC_t*)ADC1_BASE)
#define FLASH_ACR (*(volatile uint32_t*)FLASH_ACR_ADDR)
#endif
