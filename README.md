# 🌦️ Weather Agent (LLM + Tool Calling + Fallback)

An intelligent CLI-based AI agent that answers user queries using **LLM reasoning + tool calling**, with automatic fallback from OpenAI to Gemini when needed.

---

## 🚀 Features

- 🤖 LLM-based reasoning (START → PLAN → TOOL → OBSERVE → OUTPUT)
- 🛠️ Tool calling support (Weather API)
- 🔄 Automatic fallback:
  - OpenAI → Gemini (if quota/error)
- 🌐 Real-time weather data using `wttr.in`
- 🧠 Structured JSON output using Pydantic
- 💬 Interactive CLI chatbot

---

## 🏗️ Tech Stack

- Python 3.12+
- OpenAI API
- Google Gemini API (OpenAI-compatible mode)
- Pydantic
- Requests
- dotenv

---

## 📂 Project Structure

```
weather-agent/
│── api/
│   └── app.py
|   └── index.py
│── venv/
│── .env
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```
git clone <your-repo-url>
cd weather-agent
```

---

### 2️⃣ Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
```

---

## ▶️ Run the Project

```
python3 api/index.py
```

or

```
python3 api/app.py
```

---

## 💡 How It Works

### 🧠 Agent Flow

```
START → PLAN → TOOL → OBSERVE → OUTPUT
```

---

### 🛠️ Tool Example

```
get_weather(city: str)
```

---

## 🧪 Example Usage

```
👉 what is the weather of delhi?
🧠 Planning...
🔧 Calling tool get_weather
🤖 The current weather in Delhi is 30°C with clear sky
```

---

## 📌 Future Improvements

- 🔁 Retry mechanism with backoff
- 🌍 Multiple tools (news, maps, etc.)
- 📊 Logging & monitoring
- 🌐 Web UI (React + FastAPI)
- 🧠 Multi-model routing

---

## 🙌 Acknowledgements

- OpenAI
- Google AI
- wttr.in weather service

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Hritik Chauhan
