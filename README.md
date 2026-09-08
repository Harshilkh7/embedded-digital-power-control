# Embedded Digital Power Control & AI-Assisted Firmware Validation Platform

Simulation-first embedded firmware and digital power-control project designed around the kind of work expected in an embedded/power-control internship.

## 🚀 Live Demo

**Interactive control dashboard:**
https://harshilkh7.github.io/embedded-digital-power-control/

The dashboard runs a browser-based buck-converter model where you can change `Vin`, `Vref`, load, `Kp` and `Ki`, then inspect the resulting output-voltage response and regulation metrics.

> The live dashboard is a portfolio simulation. It is not a physical hardware measurement and does not claim real-board validation.

## What the project demonstrates

### Embedded digital power control

- **Embedded C / STM32F103C8:** register-level GPIO, PWM, ADC, UART, SPI and I²C initialization
- **Digital control:** discrete PI controller with output limiting and anti-windup
- **Power electronics:** averaged buck-converter plant model
- **MCU simulation:** Wokwi project configuration for STM32 firmware

### AI-assisted embedded firmware validation

- **Python validation:** automated regulation, load-step, protection and protocol tests
- **Fault injection:** over-voltage, under-voltage and over-current validation cases
- **Requirement-driven test generation:** natural-language requirement → candidate embedded test scenarios
- **Validation runner:** executes scenarios against a deterministic firmware/device model
- **Log analysis:** aggregates pass/fail results and validation metrics
- **CI:** pytest checks through GitHub Actions
- **Automated reporting:** command-line validation summary and engineering report tooling

The AI-assisted validation layer is intentionally part of the same project: it validates the behaviors implemented by the embedded power-control firmware.

## Architecture

```text
                    Vref
                     |
                     v
             +-------------------+
             | Digital PI Control|
             +---------+---------+
                       |
                     duty
                       v
             +-------------------+
             |    PWM / TIM2     |
             +---------+---------+
                       |
                       v
             +-------------------+
             |  Buck Converter   |
             |   Python model    |
             +---------+---------+
                       |
                      Vout
                       |
                       v
             +-------------------+
             |       ADC         |
             +---------+---------+
                       |
                       +-------> feedback

Requirement -> AI-assisted test generation -> Python runner
                                      |
                                      v
                         firmware/device simulation
                                      |
                         fault injection + protocol
                                      |
                                      v
                           logs -> analysis -> report
```

## Repository structure

```text
embedded-digital-power-control/
├── automation/              # Test generation + protocol utilities
│   ├── ai_test_generator.py
│   └── protocol.py
├── control/                 # PI controller + buck model
├── docs/                    # Dashboard + design documentation
├── firmware/                # Bare-metal STM32F103C8 firmware
│   ├── inc/
│   └── src/
├── simulation/wokwi/        # Wokwi MCU simulation configuration
├── validation/              # Integrated firmware validation framework
│   ├── firmware_sim.py
│   ├── fault_injection.py
│   ├── log_analyzer.py
│   └── test_runner.py
├── tests/                   # Automated validation suite
├── tools/                   # Validation CLI + engineering reports
└── .github/workflows/       # CI
```

## Run validation

```bash
pip install -r requirements.txt
pytest -q
python tools/run_validation.py
python tools/generate_report.py
```

The repository contains automated tests covering controller behavior, buck regulation/load-step response, protection behavior, protocol integrity, firmware behavior and the end-to-end validation runner.

## Build the STM32 firmware

Install the ARM GNU embedded toolchain (`arm-none-eabi-gcc`), then:

```bash
cd firmware
make
```

The build produces:

```text
firmware/build/firmware.elf
firmware/build/firmware.bin
firmware/build/firmware.hex
```

The Wokwi configuration references the generated ELF image.

## AI-assisted validation design

`automation/ai_test_generator.py` defines the GenAI boundary. It converts an engineering requirement into candidate test specifications. A deterministic fallback is included so the repository remains runnable without an external API key. An approved LLM API can replace that boundary without changing the validation runner.

See [`docs/validation_architecture.md`](docs/validation_architecture.md) for the complete validation flow.

## Firmware design notes

- System clock is configured for **72 MHz** from the 8 MHz HSE using PLL ×9.
- `PA0` is used for `TIM2_CH1` PWM.
- `PA1` is used for `ADC1_IN1` feedback, avoiding a PWM/ADC pin conflict.
- USART1 uses the 72 MHz APB2 clock for the configured baud rate.
- APB1 runs at 36 MHz, matching the I²C timing configuration.

## Resume-ready descriptions

**Embedded Digital Power Control Platform**

> Developed a simulation-based STM32 digital power-control platform with register-level peripheral drivers, digital PI regulation, buck-converter modeling, Python/pytest validation, fault injection and performance analysis.

**AI-Assisted Embedded Firmware Validation Framework**

> Extended the embedded power-control platform with Python/pytest automation, requirement-driven test generation, fault injection, protocol validation, log analysis and CI-based regression testing.

**Important:** no physical hardware measurements are claimed.

## Technologies

`C` · `Embedded C` · `STM32` · `Python` · `NumPy` · `pytest` · `Digital Control` · `PWM` · `ADC` · `UART` · `SPI` · `I²C` · `Wokwi` · `GitHub Actions` · `JavaScript` · `GitHub Pages` · `GenAI`
