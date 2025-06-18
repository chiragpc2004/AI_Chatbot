
# 💬 OpenRouter Streamlit Chatbot

This is a simple and powerful chatbot web application built using [Streamlit](https://streamlit.io/) and [OpenRouter](https://openrouter.ai/) with the `openai` Python SDK. It supports interactive chat with memory using models like DeepSeek's Qwen3.

---

## 🚀 Features

- 🔁 Persistent chat history (session state)
- 🧠 Powered by OpenRouter + `openai` SDK
- 💻 Clean web UI with Streamlit
- 🔐 Uses `.env` or Streamlit Cloud secrets for API key management

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/openrouter-chatbot
cd openrouter-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```bash
touch .env
```

And add your API key:

```
OPENROUTER_API_KEY=sk-or-your-api-key-here
```

---

## 🧪 Run Locally

```bash
streamlit run main.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push to a GitHub repo.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub → Select your repo.
4. In **"Advanced settings"**, add the environment variable:

```
OPENROUTER_API_KEY=sk-or-your-api-key-here
```

---

## 📝 Example Prompt

> You: Hello!  
>  
> AI: Hi there! How can I assist you today?

---

## 📄 File Structure

```
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📬 License

MIT License. Feel free to fork, improve, and share!

---

**Made with ❤️ using Streamlit + OpenRouter**
