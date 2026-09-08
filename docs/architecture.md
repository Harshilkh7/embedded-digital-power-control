# Architecture

The firmware side is organized into four layers:

1. **ESP32 hardware abstraction** — Arduino-ESP32 APIs expose GPIO, PWM, ADC, UART, SPI and I²C.
2. **Peripheral drivers** — `drivers.cpp` provides a small project-specific interface around those peripherals.
3. **Digital control** — the discrete PI controller calculates the PWM command from ADC feedback.
4. **Application loop** — the ESP32 samples feedback, updates control and drives the power-stage command.

The control loop is represented as:

```text
Vref -> PI Controller -> PWM -> Buck Converter -> Vout -> ADC -> PI Controller
```

The Python side provides the averaged buck plant, controller validation, performance metrics, fault injection and protocol tests.

The validation side extends the same project:

```text
Requirement
    -> AI-assisted test generation
    -> automated runner
    -> firmware/device model
    -> fault injection
    -> log analysis
    -> regression report
```

The GenAI component is an integration boundary with a deterministic fallback, so validation remains reproducible without an external API.
