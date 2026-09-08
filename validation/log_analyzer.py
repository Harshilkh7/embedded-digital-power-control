"""Convert validation events into a compact engineering summary."""
def summarize(events):
    passed = sum(event.get("status") == "PASS" for event in events)
    failed = sum(event.get("status") == "FAIL" for event in events)
    return {
        "total": len(events),
        "passed": passed,
        "failed": failed,
        "pass_rate_percent": (passed / len(events) * 100) if events else 0.0,
    }
