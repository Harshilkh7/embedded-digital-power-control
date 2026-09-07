.syntax unified
.cpu cortex-m3
.thumb
.global Reset_Handler
.global _estack
.section .isr_vector,"a",%progbits
.word _estack
.word Reset_Handler
.rept 14
.word Reset_Handler
.endr
.text
Reset_Handler:
    bl main
1:  b 1b
