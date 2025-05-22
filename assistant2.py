Here are the contents for the file `/voice-assistant/voice-assistant/assistant2.py`:

import speech_recognition as sr
import pyttsx3
import requests
import json


WAKE_WORD = "hey Jarvis"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except:
            return ""


def chat_with_ai(user_input):

    api_key = "{YOUR API KEY}"  # Replace with your real key

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "{https:}",  # Replace with your own domain or GitHub link
        "X-Title": "Test Chat",
    }

    data = {
        "model": "openai/gpt-3.5-turbo-0613",  
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    result = response.json()


    return result["choices"][0]["message"]["content"]


def main():
    speak("Jarvis is online. say 'Hey Jarvis' to activate.")

    while True:
        print("\n[ Waiting for activation... ]")
        print("speak the wake word now...")
        heard = listen()
        if WAKE_WORD in heard or True:  
            speak("Yes Aditya, I’m listening...")
            user_query = ""
            while user_query not in ["stop", "exit", "goodbye"]:

                user_query = listen()
                if user_query:
                    response = chat_with_ai(user_query)
                    speak(response)
                else:
                    speak("Sorry, I didn't catch that.")
            if user_query in ["stop", "exit", "goodbye"]:
                    speak("Goodbye Aditya. Jarvis powering off.")
                    break

if __name__ == "__main__":
    main()
