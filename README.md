# Embedded Digital Power Control & AI-Assisted Firmware Validation Platform

Simulation-first **ESP32** embedded firmware and digital power-control project combining closed-loop control, peripheral integration and automated firmware validation.

## 🚀 Live Demo

**Interactive control and validation dashboard:**
https://harshilkh7.github.io/embedded-digital-power-control/

The dashboard provides a browser-based buck-converter model plus an interactive demonstration of the AI-assisted firmware validation pipeline.

> The live dashboard is a portfolio simulation. It is not a physical hardware measurement and does not claim real-board power-stage validation.

## What the project demonstrates

### Embedded digital power control

- **ESP32 DevKit:** C++ firmware using the Arduino-ESP32 framework
- **Peripherals:** GPIO, PWM, ADC, UART, SPI and I²C
- **Digital control:** discrete PI controller with output limiting and anti-windup
- **Power electronics:** averaged buck-converter plant model
- **MCU simulation:** Wokwi ESP32 DevKit simulation
- **Build system:** PlatformIO with ESP32 CI compilation

### AI-assisted embedded firmware validation

- **Python validation:** automated regulation, load-step, protection and protocol tests
- **Fault injection:** over-voltage, under-voltage and over-current validation cases
- **Requirement-driven test generation:** natural-language requirement → candidate embedded test scenarios
- **Validation runner:** executes scenarios against a deterministic firmware/device model
- **Log analysis:** aggregates pass/fail results and validation metrics
- **CI:** pytest regression checks plus ESP32 firmware compilation through GitHub Actions
- **Automated reporting:** command-line validation summary and engineering report tooling

The AI-assisted validation layer is intentionally part of the same project: it validates the behaviors implemented by the ESP32 embedded power-control firmware.

## Architecture

```text
                         ESP32
                           |
          +----------------+----------------+
          |                |                |
         ADC              PWM          UART/SPI/I²C
          |                |
          v                v
       Vout feedback   Digital PI Controller
                           |
                           v
                    Buck Converter
                           |
                          Vout
                           |
                           +------> ADC feedback

Requirement -> AI-assisted test generation -> Python runner
                                      |
                                      v
                             ESP32 firmware model
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
├── firmware/                # ESP32 PlatformIO firmware
│   ├── inc/
│   ├── src/
│   └── platformio.ini
├── simulation/wokwi/        # Wokwi ESP32 simulation configuration
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

## Build the ESP32 firmware

Install PlatformIO, then:

```bash
cd firmware
pio run
```

The compiled firmware is produced under:

```text
firmware/.pio/build/esp32dev/firmware.bin
```

The Wokwi configuration points to this ESP32 firmware image.

## ESP32 firmware pin map

| Function | ESP32 pin |
|---|---:|
| Status LED | GPIO 2 |
| PWM output | GPIO 25 |
| ADC feedback | GPIO 34 |
| I²C SDA | GPIO 21 |
| I²C SCL | GPIO 22 |
| SPI SCK | GPIO 18 |
| SPI MISO | GPIO 19 |
| SPI MOSI | GPIO 23 |
| SPI CS | GPIO 5 |
| UART | USB serial / Serial |

GPIO 34 is used only as an ADC input, while GPIO 25 provides the PWM control signal.

## AI-assisted validation design

`automation/ai_test_generator.py` defines the GenAI boundary. It converts an engineering requirement into candidate test specifications. A deterministic fallback is included so the repository remains runnable without an external API key. An approved LLM API can replace that boundary without changing the validation runner.

See [`docs/validation_architecture.md`](docs/validation_architecture.md) for the complete validation flow.

## Resume-ready descriptions

**Embedded Digital Power Control Platform**

> Developed a simulation-based ESP32 digital power-control platform with C++ peripheral integration, digital PI regulation, buck-converter modeling, Python/pytest validation, fault injection and performance analysis.

**AI-Assisted Embedded Firmware Validation Framework**

> Extended the ESP32 power-control platform with Python/pytest automation, requirement-driven test generation, fault injection, protocol validation, log analysis and CI-based regression testing.

**Important:** no physical hardware measurements are claimed.

## Technologies

`C++` · `ESP32` · `Arduino-ESP32` · `PlatformIO` · `Python` · `NumPy` · `pytest` · `Digital Control` · `PWM` · `ADC` · `UART` · `SPI` · `I²C` · `Wokwi` · `GitHub Actions` · `JavaScript` · `GitHub Pages` · `GenAI`
