# Embedded Digital Power Control & Automated Firmware Validation Platform

Simulation-first portfolio project for an embedded firmware / power-control internship.

## Components
- STM32F103C8 firmware in embedded C
- Register-level GPIO, PWM, UART, SPI, I2C and ADC interfaces
- Discrete digital PI voltage controller
- Averaged buck-converter model in Python
- pytest validation and fault injection
- Automated engineering report generation
- GenAI test-generation interface
- Wokwi configuration for MCU simulation
- GitHub Actions CI

## Run the software validation
```bash
pip install -r requirements.txt
pytest -q
python tools/generate_report.py
```

## Build firmware
Install `arm-none-eabi-gcc`, then:
```bash
cd firmware
make
```

The resulting `build/firmware.elf` is referenced by the Wokwi configuration.

## Honest resume wording
"Developed a simulation-based STM32 digital power-control platform with
register-level peripheral drivers, digital PI regulation, Python/pytest
validation, fault injection and automated performance analysis."

No physical hardware measurements are claimed.
