# AI-Assisted Embedded Firmware Validation

The validation layer is built around the embedded power-control firmware rather than being a separate application.

```text
Requirement
    ↓
GenAI-assisted test generation
    ↓
Python test runner
    ↓
Firmware/device simulation
    ↓
Fault injection + protocol checks
    ↓
Logs and pass/fail results
    ↓
Automated analysis/reporting
```

## What is automated

- Nominal regulation behavior
- Load-step recovery scenario
- Over-voltage, under-voltage and over-current faults
- PWM boundary checks
- Protocol/CRC integrity
- Result aggregation and pass-rate calculation

## GenAI boundary

`automation/ai_test_generator.py` provides the interface between natural-language requirements and candidate test specifications. The repository uses a deterministic fallback so the project runs without an API key. An approved LLM API can replace that boundary without changing the test runner.

## Why this belongs with the power-control project

The same project supplies the firmware, controller and simulated plant. The validation framework exercises those behaviors and turns engineering requirements into repeatable automated tests. This demonstrates both embedded development and validation automation.
