from dataclasses import dataclass

@dataclass
class Protection:
    uvlo: float = 2.7
    ovlo: float = 3.6
    oc: float = 2.5
    def evaluate(self, voltage, current):
        if voltage > self.ovlo: return "OVERVOLTAGE"
        if voltage < self.uvlo: return "UNDERVOLTAGE"
        if current > self.oc: return "OVERCURRENT"
        return "OK"

def test_protection():
    p = Protection()
    assert p.evaluate(3.3, 1) == "OK"
    assert p.evaluate(4, 1) == "OVERVOLTAGE"
    assert p.evaluate(2, 1) == "UNDERVOLTAGE"
    assert p.evaluate(3.3, 3) == "OVERCURRENT"
