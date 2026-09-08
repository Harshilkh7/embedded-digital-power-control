"""Execute generated and fault-injection validation scenarios."""
from automation.ai_test_generator import generate_tests
from validation.firmware_sim import FirmwareDevice
from validation.fault_injection import faults
from validation.log_analyzer import summarize

def run_validation(requirement="Validate a 3.3 V embedded power controller"):
    device = FirmwareDevice()
    events = []
    for spec in generate_tests(requirement):
        if spec.name == "nominal_regulation":
            state = device.apply_measurement(3.30, 0.5)
            ok = state == "REGULATING"
        elif spec.name == "load_step":
            device.apply_measurement(3.30, 0.5)
            state = device.apply_measurement(3.25, 1.0)
            ok = state == "REGULATING"
        elif spec.name == "over_voltage":
            state = device.apply_measurement(3.80, 0.5)
            ok = state == "OVERVOLTAGE"
        else:
            state, ok = "UNKNOWN", False
        events.append({"name": spec.name, "status": "PASS" if ok else "FAIL", "state": state})

    for fault in faults():
        state = device.apply_measurement(fault["voltage"], fault["current"])
        events.append({"name": fault["name"], "status": "PASS" if state == fault["expected"] else "FAIL", "state": state})
    return events, summarize(events)

if __name__ == "__main__":
    events, summary = run_validation()
    print(summary)
    for event in events:
        print(f"{event['status']}: {event['name']} -> {event['state']}")
