"""
AI Study Assistant - a simple command-line chatbot for beginner students.

Features:
- Loads HF_TOKEN and MODEL_ID from a .env file (never hard-coded).
- Beginner-friendly system message that shapes how the assistant answers.
- Keeps asking questions until the user types 'exit' or 'quit'.
- Rejects empty questions with a clear message.
- Maintains recent conversation history so follow-up questions make sense.
- 'clear' resets the conversation history.
- Lets the user set a temperature between 0.1 and 1.0.
- Includes one example of a JSON-only prompt whose reply is parsed with json.loads().
"""

import os
import sys
import json

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# ---------------------------------------------------------------------------
# 1. Secure configuration: load secrets from .env, never from source code
# ---------------------------------------------------------------------------
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = os.getenv("MODEL_ID")

if not HF_TOKEN or not MODEL_ID:
    print("Error: HF_TOKEN and MODEL_ID must both be set in your .env file.")
    print("Copy .env.example to .env and fill in your own values.")
    sys.exit(1)

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

# ---------------------------------------------------------------------------
# 2. Beginner-friendly system message (role, task, context, constraints, format)
# ---------------------------------------------------------------------------
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a friendly AI Study Assistant helping a beginner student. "
        "Task: answer study questions clearly and patiently. "
        "Context: the student may not know technical terms yet. "
        "Constraints: explain any jargon you use, keep answers under about "
        "150 words unless the student explicitly asks for more detail, and "
        "give one short example whenever it helps understanding. "
        "Format: plain, well-organized sentences or a short bullet list."
    ),
}


def get_temperature() -> float:
    """Ask the user for a temperature value between 0.1 and 1.0, with validation."""
    while True:
        raw = input("Set temperature (0.1 - 1.0) [default 0.7]: ").strip()
        if raw == "":
            return 0.7
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a number, e.g. 0.7")
            continue
        if 0.1 <= value <= 1.0:
            return value
        print("Temperature must be between 0.1 and 1.0.")


def ask_model(messages, temperature: float) -> str:
    """Send a chat request to the Hugging Face model and return the answer text."""
    try:
        response = client.chat_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=400,
        )
        return response.choices[0].message.content
    except Exception as exc:
        # Readable error handling instead of a raw traceback
        return f"[Sorry, something went wrong talking to the model: {exc}]"


def demo_json_prompt(temperature: float) -> None:
    """
    One example of a JSON-only prompt. We ask the model to reply with ONLY
    valid JSON in a fixed shape, then parse it with json.loads().
    """
    topic = input("Enter a topic for a structured JSON study card: ").strip()
    if not topic:
        print("Topic cannot be empty.\n")
        return

    json_messages = [
        SYSTEM_MESSAGE,
        {
            "role": "user",
            "content": (
                f"Create a short study card about '{topic}'. "
                "Respond with ONLY valid JSON, no extra text and no markdown "
                "fences, using exactly this shape: "
                '{"topic": string, "summary": string, '
                '"key_points": [string, string, string]}'
            ),
        },
    ]

    raw = ask_model(json_messages, temperature)
    # print("\n--- Raw model reply ---")
    # print(raw, "\n")
    try:
        cleaned = raw.strip().strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:].strip()
        data = json.loads(cleaned)
        # print("Parsed JSON data:")
        # print(json.dumps(data, indent=2))

        print("\n--- Study Card ---")
        print("Topic:", data.get("topic"))
        print("Summary:", data.get("summary"))
        print("Key points:")
        for point in data.get("key_points", []):
            print(" -", point)
        print()
    except json.JSONDecodeError:
        print("Could not parse the model's reply as JSON. Raw reply was:")
        print(raw, "\n")


def main() -> None:
    print("=== AI Study Assistant ===")
    print("Type a question to get help.")
    print("Commands: 'clear' resets history, 'json' runs a structured demo, "
          "'exit' or 'quit' ends the program.\n")

    temperature = get_temperature()
    history = [SYSTEM_MESSAGE]

    while True:
        question = input("You: ").strip()

        # Reject empty questions
        if question == "":
            print("Please enter a question - it cannot be empty.\n")
            continue

        if question.lower() in ("exit", "quit"):
            print("Goodbye! Happy studying.")
            break

        if question.lower() == "clear":
            history = [SYSTEM_MESSAGE]
            print("Conversation history cleared.\n")
            continue

        if question.lower() == "json":
            demo_json_prompt(temperature)
            continue

        history.append({"role": "user", "content": question})

        # Keep only recent history (system message + last 10 turns) so the
        # request stays small and fast.
        trimmed_history = [history[0]] + history[-10:]

        answer = ask_model(trimmed_history, temperature)
        print(f"Assistant: {answer}\n")

        history.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()