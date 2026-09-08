"""Convert validation events into a compact engineering summary."""
def summarize(events):
    passed = sum(event.get("status") == "PASS" for event in events)
    failed = sum(event.get("status") == "FAIL" for event in events)
    pass_rate = round((passed / len(events) * 100), 2) if events else 0.0
    return {
        "total": len(events),
        "passed": passed,
        "failed": failed,
        "pass_rate_percent": pass_rate,
    }
