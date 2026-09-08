"""CLI entry point for the integrated firmware validation framework."""
from validation.test_runner import run_validation

if __name__ == "__main__":
    events, summary = run_validation()
    print("Embedded Firmware Validation")
    print("=" * 28)
    for event in events:
        print(f"{event['status']:<4} {event['name']:<24} {event['state']}")
    print("-" * 28)
    print(f"Passed: {summary['passed']}/{summary['total']}")
    print(f"Pass rate: {summary['pass_rate_percent']:.1f}%")
