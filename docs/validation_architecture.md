# AI-Assisted ESP32 Embedded Firmware Validation

The validation layer is built around the **ESP32 DevKit power-control firmware** rather than being a separate application.

```text
Engineering Requirement
        ↓
GenAI-assisted test generation
        ↓
Python validation runner
        ↓
ESP32 firmware/device behavior model
        ↓
Fault injection + protocol checks
        ↓
Logs and pass/fail results
        ↓
Automated analysis/reporting
        ↓
GitHub Actions regression validation
```

## What is automated

- ESP32 nominal regulation behavior
- Load-step recovery scenario
- Over-voltage, under-voltage and over-current faults
- PWM boundary checks
- Protocol/CRC integrity
- Result aggregation and pass-rate calculation
- Regression testing in CI

## ESP32 validation boundary

The Python validation model represents the externally observable behavior of the ESP32 firmware: regulation state, sensed output voltage, protection states and PWM command limits. It allows repeatable validation without requiring a physical ESP32 board for every test run.

The actual embedded target is an ESP32 DevKit firmware project built with PlatformIO and Arduino-ESP32. The same project exposes GPIO, PWM, ADC, UART, SPI and I²C interfaces.

## GenAI boundary

`automation/ai_test_generator.py` provides the interface between natural-language engineering requirements and candidate ESP32 test specifications. The repository uses a deterministic fallback so the project runs without an API key. An approved LLM API can replace that boundary without changing the validation runner.

## Why this belongs with the power-control project

The same project supplies the ESP32 firmware, digital controller and simulated plant. The validation framework exercises those behaviors and turns engineering requirements into repeatable automated tests. This demonstrates embedded development, power-control validation and GenAI-assisted automation as one coherent system.
