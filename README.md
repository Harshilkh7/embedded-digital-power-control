# Embedded Digital Power Control & Automated Firmware Validation Platform

Simulation-first embedded firmware and digital power-control project designed around the kind of work expected in an embedded/power-control internship.

## 🚀 Live Demo

**Interactive control dashboard:**
https://harshilkh7.github.io/embedded-digital-power-control/

The dashboard runs a browser-based buck-converter model where you can change `Vin`, `Vref`, load, `Kp` and `Ki`, then inspect the resulting output-voltage response and regulation metrics.

> The live dashboard is a portfolio simulation. It is not a physical hardware measurement and does not claim real-board validation.

## What the project demonstrates

- **Embedded C / STM32F103C8:** register-level GPIO, PWM, ADC, UART, SPI and I²C initialization
- **Digital control:** discrete PI controller with output limiting and anti-windup
- **Power electronics:** averaged buck-converter plant model
- **Python validation:** automated regulation, load-step, protection and protocol tests
- **Fault injection:** over-voltage, under-voltage and over-current validation cases
- **GenAI-assisted validation:** natural-language requirement → candidate embedded test scenarios
- **MCU simulation:** Wokwi project configuration for STM32 firmware
- **CI:** pytest checks through GitHub Actions
- **Live engineering dashboard:** static GitHub Pages site with an interactive JavaScript simulation

## Architecture

```text
             +-------------------+
 Vref ------>| Digital PI Control |---- duty ----> PWM
             +-------------------+                  |
                      ^                             v
                      | ADC feedback       +---------------+
                      +---------------------| Buck Converter|
                                            +---------------+
                                                   |
                                                  Vout
```

The repository separates the physical concepts into three layers:

1. **Firmware layer** — STM32 peripheral drivers and the embedded control loop.
2. **Plant/control layer** — Python model of the converter and controller response.
3. **Validation layer** — pytest, fault injection, protocol checks and automated reporting.

## Repository structure

```text
embedded-digital-power-control/
├── automation/          # Test generation and protocol utilities
├── control/             # PI controller and buck model
├── docs/                # GitHub Pages live dashboard + design notes
├── firmware/            # Bare-metal STM32F103C8 firmware
│   ├── inc/
│   └── src/
├── simulation/wokwi/    # Wokwi MCU simulation configuration
├── tests/               # Automated validation suite
├── tools/               # Engineering report generation
└── .github/workflows/   # CI
```

## Run the Python validation

```bash
pip install -r requirements.txt
pytest -q
python tools/generate_report.py
```

The current validation suite contains **8 automated tests** covering controller behavior, buck regulation/load-step response, protection behavior and protocol integrity.

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

### Firmware design notes

- System clock is configured for **72 MHz** from the 8 MHz HSE using PLL ×9.
- `PA0` is used for `TIM2_CH1` PWM.
- `PA1` is used for `ADC1_IN1` feedback, avoiding a PWM/ADC pin conflict.
- USART1 uses the 72 MHz APB2 clock for the configured baud rate.
- APB1 runs at 36 MHz, matching the I²C timing configuration.

## MCU simulation

Open the Wokwi project configuration under `simulation/wokwi/` after building the firmware. The project is intended to demonstrate firmware/peripheral behavior in simulation; the converter response shown on the live dashboard is a separate mathematical model.

## Resume-ready description

> Developed a simulation-based STM32 digital power-control platform with register-level peripheral drivers, digital PI regulation, Python/pytest validation, fault injection, automated performance analysis and a live browser-based control dashboard.

**Important:** no physical hardware measurements are claimed.

## Technologies

`C` · `Embedded C` · `STM32` · `Python` · `NumPy` · `pytest` · `Digital Control` · `PWM` · `ADC` · `UART` · `SPI` · `I²C` · `Wokwi` · `GitHub Actions` · `JavaScript` · `GitHub Pages`
