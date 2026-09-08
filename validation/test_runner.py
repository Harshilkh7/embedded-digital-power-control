"""Execute requirement-driven and fault-injection validation scenarios."""
from automation.ai_test_generator import generate_tests
from validation.firmware_sim import FirmwareDevice
from validation.fault_injection import faults
from validation.log_analyzer import summarize


def run_validation(requirement="Validate a 3.3 V ESP32 embedded power controller"):
    device = FirmwareDevice()
    events = []

    for spec in generate_tests(requirement):
        if spec.name == "nominal_regulation":
            state = device.apply_measurement(3.30, 0.50)
            ok = state == "REGULATING" and abs(device.vout - 3.30) <= 0.02
        elif spec.name == "load_step":
            device.apply_measurement(3.30, 0.50)
            state = device.apply_measurement(3.25, 1.00)
            ok = state == "REGULATING"
        elif spec.name == "over_voltage":
            state = device.apply_measurement(3.80, 0.50)
            ok = state == "OVERVOLTAGE" and device.pwm_duty == 0.0
        elif spec.name == "under_voltage":
            state = device.apply_measurement(2.50, 0.50)
            ok = state == "UNDERVOLTAGE" and device.pwm_duty == 0.0
        elif spec.name == "over_current":
            state = device.apply_measurement(3.30, 2.50)
            ok = state == "OVERCURRENT" and device.pwm_duty == 0.0
        elif spec.name == "pwm_bounds":
            low = device.set_pwm(-0.10)
            high = device.set_pwm(1.20)
            state, ok = "REGULATING", low == 0.0 and high == 0.95
        else:
            state, ok = "UNKNOWN", False
        events.append({"name": spec.name, "status": "PASS" if ok else "FAIL", "state": state})

    for fault in faults():
        state = device.apply_measurement(fault["voltage"], fault["current"])
        ok = state == fault["expected"] and device.pwm_duty == 0.0
        events.append({"name": fault["name"], "status": "PASS" if ok else "FAIL", "state": state})

    return events, summarize(events)


if __name__ == "__main__":
    events, summary = run_validation()
    print("ESP32 Firmware Validation")
    print("=" * 25)
    print(summary)
    for event in events:
        print(f"{event['status']}: {event['name']} -> {event['state']}")
