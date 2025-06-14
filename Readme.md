# 🗣️ Whisper + GPT Summary Assistant

A simple voice-to-summary assistant built using OpenAI Whisper for speech recognition and GPT-3.5-turbo for summarization.

---

## ✨ Features

- 🎧 Converts speech (audio file) into text using Whisper  
- ✂️ Summarizes the transcribed text via OpenAI GPT  
- 🧪 Fully script-based, runs locally  
- 💻 Developed on macOS with Python (Anaconda environment)

---

## 📂 Project Structure

```
STTProject/
├── backend/
│   ├── app.py              # Main execution file (STT + GPT summary)
│   ├── audio_sample.mp3    # Sample audio input
│   └── summarize_module.py # GPT logic module
├── .env                    # API key (not tracked by Git)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Install ffmpeg (required by Whisper):

```bash
brew install ffmpeg
```

---

## 🔐 .env file format

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Make sure your key is valid. `sk-proj-...` keys may not work for GPT endpoints.

---

## ▶️ How to Run

```bash
python backend/app.py
```

- Loads Whisper model  
- Transcribes `audio_sample.mp3`  
- Summarizes the result using GPT  
- Displays everything in terminal

---

## 📌 Notes

GPT-based summarization may fail if you’re using a restricted `sk-proj-...` key.  
**Recommended:** use a personal `sk-...` key created from [OpenAI’s API page](https://platform.openai.com/account/api-keys).

---

## 🧑‍💻 Developer Notes

This project was developed as a prototype assistant for voice summarization.  
I worked entirely in macOS, focused on fast local testing using Whisper and OpenAI’s GPT.  
Next goals include real-time audio input and Flask API deployment.
