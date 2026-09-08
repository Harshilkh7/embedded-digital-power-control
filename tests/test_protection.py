from dataclasses import dataclass


@dataclass
class Protection:
    uvlo: float = 2.80
    ovlo: float = 3.63
    oc: float = 2.00

    def evaluate(self, voltage, current):
        if voltage > self.ovlo:
            return "OVERVOLTAGE"
        if voltage < self.uvlo:
            return "UNDERVOLTAGE"
        if current > self.oc:
            return "OVERCURRENT"
        if voltage < 3.00 or voltage > 3.50 or current > 1.50:
            return "WARNING"
        return "OK"


def test_protection_states():
    p = Protection()
    assert p.evaluate(3.3, 1.0) == "OK"
    assert p.evaluate(3.55, 1.0) == "WARNING"
    assert p.evaluate(4.0, 1.0) == "OVERVOLTAGE"
    assert p.evaluate(2.5, 1.0) == "UNDERVOLTAGE"
    assert p.evaluate(3.3, 2.5) == "OVERCURRENT"
