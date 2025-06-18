# 🧠 CLI Chatbot using OpenRouter AI

This is a simple Python-based command-line chatbot that uses [OpenRouter](https://openrouter.ai/) as the backend for AI-powered responses. It uses the `openai` Python SDK to interact with custom models hosted via OpenRouter, such as DeepSeek's `qwen3-8b`.

---

## 🚀 Features

- Communicates with OpenRouter's AI models
- Runs in the terminal (CLI)
- Easy to customize model and prompt behavior
- Exit anytime with `exit`, `quit`, or `bye`

---

## 🛠️ Requirements

- Python 3.7+
- `openai` Python package

Install dependencies:

```bash
pip install openai
```

---

## 🧾 Usage

1. **Update the script** with your API key (from [OpenRouter](https://openrouter.ai/)).
2. Run the chatbot:

```bash
python chatbot.py
```

3. Type your questions or prompts.
4. Exit with: `exit`, `quit`, or `bye`.

---

## 📄 Example

```bash
You: What's the capital of France?
AI: The capital of France is Paris.

You: bye
Exiting the chat.
```

---

## 🔐 Security Note

Do **not** hardcode or share your API keys in public repositories. Use `.env` files or environment variables in production.

---

## 💡 Tip

You can change the model by modifying the line:

```python
model="deepseek/deepseek-r1-0528-qwen3-8b:free"
```

Check [OpenRouter Models](https://openrouter.ai/docs) for more options.

---

## 📬 License

This project is licensed under the MIT License.
