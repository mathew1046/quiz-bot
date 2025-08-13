# 📚 Quiz Bot

A simple web app that generates multiple-choice questions from syllabus text using Google's Gemini API.

---

## 🚀 Features
- Generates MCQs from any given syllabus or topic.
- Uses **Gemini 2.5 Flash** (Generative Language API) for fast question generation.
- Displays questions, options, and correct answers in a clean UI.
- Runs locally with Flask backend and HTML/JS frontend.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Google Gemini 2.5 Flash
- **Deployment**: Docker (optional)

---

## 📂 Project Structure
```
quiz-bot/
│── static/               # CSS, JS, Images
│── templates/            # HTML templates
│── app.py                # Flask backend
│── requirements.txt      # Python dependencies
│── .env                  # API keys and environment variables
│── Dockerfile            # For containerization
│── README.md             # This file
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone this repo
```bash
git clone https://github.com/mathew1046/quiz-bot.git
cd quiz-bot
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Gemini API key  
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running Locally
```bash
python app.py
```
Then open:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Running with Docker

### Build the image
```bash
docker build -t quiz-bot .
```

### Run the container
```bash
docker run -p 5000:5000 --env-file .env quiz-bot
```

---

## 📝 Example Output
```
Q1: Which functional unit is responsible for sequencing and interpreting instructions?
• Arithmetic Logic Unit (ALU)
• Memory Unit
• Input/Output Unit
• Control Unit
Answer: Control Unit
```

---

## 🛠 Troubleshooting
- **403 Git Push Error** → Make sure your GitHub token has `repo` permissions.
- **Docker Error: Cannot connect to engine** → Ensure Docker Desktop is running.
- **Couldn't parse AI response** → Check your Gemini output format; ensure it's valid JSON.

---

## 📜 License
© 2025 Mathew Joseph
