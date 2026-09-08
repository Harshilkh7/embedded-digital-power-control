from automation.ai_test_generator import generate_tests
from validation.firmware_sim import FirmwareDevice
from validation.fault_injection import faults
from validation.log_analyzer import summarize
from validation.test_runner import run_validation


def test_esp32_target():
    assert FirmwareDevice().target == "ESP32 DevKit"


def test_nominal_firmware_regulation():
    device = FirmwareDevice()
    assert device.apply_measurement(3.3, 0.5) == "REGULATING"


def test_warning_state():
    device = FirmwareDevice()
    assert device.apply_measurement(3.55, 0.5) == "WARNING"


def test_protection_disables_pwm():
    device = FirmwareDevice()
    device.set_pwm(0.6)
    assert device.apply_measurement(3.8, 0.5) == "OVERVOLTAGE"
    assert device.pwm_duty == 0.0


def test_pwm_is_bounded():
    device = FirmwareDevice()
    assert device.set_pwm(1.5) == 0.95
    assert device.set_pwm(-1.0) == 0.0


def test_fault_injection():
    device = FirmwareDevice()
    for fault in faults():
        assert device.apply_measurement(fault["voltage"], fault["current"]) == fault["expected"]


def test_requirement_generator_contract():
    specs = generate_tests("Validate ESP32 power regulation")
    assert len(specs) == 6
    assert {spec.name for spec in specs} >= {
        "nominal_regulation", "load_step", "over_voltage", "under_voltage",
        "over_current", "pwm_bounds"
    }


def test_end_to_end_validation():
    events, summary = run_validation()
    assert summary["failed"] == 0
    assert summary["total"] == 9
    assert summary["pass_rate_percent"] == 100.0
    assert all(event["status"] == "PASS" for event in events)


def test_log_analyzer():
    summary = summarize([{"status": "PASS"}, {"status": "FAIL"}, {"status": "PASS"}])
    assert summary == {"total": 3, "passed": 2, "failed": 1, "pass_rate_percent": 66.67}
