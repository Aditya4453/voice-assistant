# Jarvis – AI Voice Assistant
While casually scrolling one day, I discovered that our laptops and computers have built-in features and software that can convert typed text into speech. That sparked an idea — what if I could reverse this? What if I say something, convert my voice into text, send that text to an AI model to get a response, and then use text-to-speech to make the system speak the answer out loud? That simple curiosity turned into a spark, and from there, I decided to start researching and building my own version of a virtual assistant.

Jarvis is a Python-based voice assistant that listens to your commands, responds with AI-generated answers, and speaks them out loud. It uses OpenRouter (ChatGPT) for generating responses, SpeechRecognition for input, and pyttsx3 for voice output.

---

## Features

- **Voice-activated**: Starts on saying "Hey Jarvis".
- **Conversational**: Continues chatting until you say “exit”, “stop”, or “goodbye”.
- **Free AI API**: Works with [OpenRouter](https://openrouter.ai/) – no OpenAI subscription needed.
- **Text-to-Speech Output**: Answers are spoken aloud using `pyttsx3`.

---

## Demo

*Coming soon: Add a GIF or YouTube video link here showing Jarvis in action.*

---

## Installation

### 1. Clone this repo

```bash
git clone https://github.com/Aditya4453/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

---

## Overview

This project uses:
- **SpeechRecognition** – to capture your voice
- **Requests & JSON** – to fetch AI responses using OpenRouter API
- **pyttsx3** – to convert AI response to spoken voice (offline text-to-speech)

Jarvis starts when you say **"Hey Jarvis"** and responds to your voice inputs. It keeps the conversation alive until you tell it to stop.

---

## Setup & Installation

### 2. Install Required Libraries

Open your terminal or command prompt and run the following commands one by one:

```bash
pip install SpeechRecognition
pip install requests
pip install pyttsx3
```

---

### 3. Get Your Free API Key from OpenRouter

Jarvis uses ChatGPT via OpenRouter. Here’s how to get your API key:

1. Go to [OpenRouter](https://openrouter.ai)
2. Create a free account.
3. Go to the API Keys section.
4. Generate a new API key and copy it.

---

### 4. Paste the API Key in the Code

Open your Python file (example: `assistant2.py`) and locate this part:

```python
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
}
```

Replace `YOUR_API_KEY_HERE` with the actual API key you copied from OpenRouter.

---

### 5. Run the Program

Now, just run your Python script:

```bash
python assistant2.py
```

Say "Hey Jarvis" to start the conversation. Then speak naturally. Jarvis will listen, reply with an AI-generated response, and speak it back to you.

To stop the assistant, simply say:

```
stop
exit
goodbye
```
