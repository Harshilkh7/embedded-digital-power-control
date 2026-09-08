# Architecture

The firmware side is organized into four layers:

1. **ESP32 hardware abstraction** — Arduino-ESP32 APIs expose GPIO, PWM, ADC, UART, SPI and I²C.
2. **Peripheral drivers** — `drivers.cpp` provides project-specific interfaces around those peripherals.
3. **Digital control** — the discrete PI controller calculates the PWM command from ADC feedback.
4. **Application loop** — the ESP32 samples voltage/current feedback, evaluates protection, updates control and drives the power-stage command.

## Control loop

```text
Vref -> PI Controller -> PWM -> Buck Converter -> Vout -> ADC -> PI Controller
                              |
                         Protection
                         /         \
                     OV / OC      UV / warning
                     PWM=0         recovery
```

## ESP32 interface map

| Function | GPIO |
|---|---:|
| Status LED | 2 |
| PWM | 25 |
| Voltage ADC | 34 |
| Current ADC | 35 |
| I²C SDA/SCL | 21 / 22 |
| SPI SCK/MISO/MOSI/CS | 18 / 19 / 23 / 5 |
| UART | USB serial |

The firmware uses a 20 kHz PWM carrier and a 1 kHz digital control update. ADC readings are converted into engineering units before protection and control logic run.

## Python validation

The Python side provides the averaged buck plant, controller validation, performance metrics, fault injection and protocol tests.

The validation side extends the same project:

```text
Engineering Requirement
    -> requirement-driven test generation
    -> automated runner
    -> ESP32 firmware/device behavior model
    -> fault injection + protocol checks
    -> log analysis
    -> pytest regression
    -> GitHub Actions
```

The GenAI component is an integration boundary with a deterministic offline fallback, so validation remains reproducible without an external API.
