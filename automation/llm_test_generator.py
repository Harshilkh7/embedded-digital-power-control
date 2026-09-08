"""Optional LLM adapter for requirement-driven embedded test generation."""
import json
import os

from automation.ai_test_generator import TestSpec


SYSTEM_PROMPT = """You generate embedded-firmware validation scenarios.
Return ONLY a JSON array. Each item must contain: name, stimulus, expected.
Keep scenarios deterministic, hardware-safe, and relevant to an ESP32 digital
power controller. Include nominal behavior, transients, protection boundaries,
communication integrity, and actuator limits when applicable."""


def generate_tests_with_llm(requirement: str) -> list[TestSpec]:
    """Use an OpenAI Responses API model when explicitly enabled.

    The normal CI path never calls the API. This adapter is opt-in through
    GENAI_TEST_GENERATOR=1 and requires OPENAI_API_KEY.
    """
    if os.getenv("GENAI_TEST_GENERATOR") != "1":
        raise RuntimeError("GenAI generation is not enabled")

    from openai import OpenAI

    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    response = client.responses.create(
        model=model,
        input=[
            {"role": "developer", "content": SYSTEM_PROMPT},
            {"role": "user", "content": requirement},
        ],
    )
    raw = json.loads(response.output_text)
    return [TestSpec(item["name"], item["stimulus"], item["expected"]) for item in raw]
