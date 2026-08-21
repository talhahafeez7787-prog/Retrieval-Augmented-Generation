# AI Study Assistant (CLI)

A simple command-line chatbot that answers study questions using a Hugging Face model.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your real values:
   ```
   cp .env.example .env
   ```
   - `HF_TOKEN`: your Hugging Face access token
   - `MODEL_ID`: a chat-capable model, e.g. `meta-llama/Meta-Llama-3-8B-Instruct`
3. Run it:
   ```
   python study_assistant.py
   ```

## Using it

- Type any study question and press Enter.
- Type `clear` to reset the conversation history.
- Type `json` to try the structured JSON-prompt demo (asks for a topic, gets
  back a parsed "study card" with a summary and key points).
- Type `exit` or `quit` to leave.
- Empty input is rejected with a message asking you to type something.

## How this maps to the rubric

- **Secure configuration (20%)** — `HF_TOKEN`/`MODEL_ID` are read via
  `os.getenv()` after `load_dotenv()`; nothing is hard-coded. `.env` is
  listed in `.gitignore` and only `.env.example` (with placeholder values)
  is committed.
- **API integration (25%)** — `InferenceClient.chat_completion()` sends the
  request to the Hugging Face model; the reply text is pulled out with
  `response.choices[0].message.content`.
- **Prompt quality (20%)** — the system message defines role (study
  assistant), task (answer questions), context (beginner student), and
  constraints/format (explain jargon, word limit, example, plain/bullet
  format).
- **Chatbot behaviour (20%)** — a `while True` loop keeps asking; `exit`/
  `quit` breaks it; `clear` resets `history`; blank input is rejected before
  it's ever sent; recent turns are kept in `history` (trimmed to the last
  10 messages plus the system message) so follow-ups have context.
- **Error handling (15%)** — missing `.env` values exit with a clear
  message before any request is made; API/network errors are caught in
  `ask_model()` and shown as a readable message instead of a crash; the
  JSON demo catches `json.JSONDecodeError` and shows the raw reply instead
  of failing silently.

## Submission checklist

- [ ] `study_assistant.py`
- [ ] `.env.example` (no real token)
- [ ] `.gitignore`
- [ ] `requirements.txt`
- [ ] Screenshot of a terminal run showing: a normal Q&A exchange, `clear`
      in action, and the `json` demo output. (Take this yourself after
      running the app locally — it can't be generated here since it
      requires your own Hugging Face token and a live run.)