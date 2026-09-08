from validation.firmware_sim import FirmwareDevice
from validation.fault_injection import faults
from validation.log_analyzer import summarize
from validation.test_runner import run_validation


def test_esp32_target():
    device = FirmwareDevice()
    assert device.target == "ESP32 DevKit"


def test_nominal_firmware_regulation():
    device = FirmwareDevice()
    assert device.apply_measurement(3.3, 0.5) == "REGULATING"


def test_pwm_is_bounded():
    device = FirmwareDevice()
    assert device.set_pwm(1.5) == 0.95
    assert device.set_pwm(-1.0) == 0.0


def test_fault_injection():
    device = FirmwareDevice()
    for fault in faults():
        assert device.apply_measurement(fault["voltage"], fault["current"]) == fault["expected"]


def test_end_to_end_validation():
    events, summary = run_validation()
    assert summary["failed"] == 0
    assert summary["total"] == 6
    assert all(event["status"] == "PASS" for event in events)


def test_log_analyzer():
    summary = summarize([{"status": "PASS"}, {"status": "FAIL"}, {"status": "PASS"}])
    assert summary == {"total": 3, "passed": 2, "failed": 1, "pass_rate_percent": 66.67}
