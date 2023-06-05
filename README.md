# Virtual Assistant

This is a virtual assistant project written in Python that uses speech recognition and text-to-speech synthesis to interact with the user. The virtual assistant, named Alexa, can perform various tasks such as playing videos on YouTube, providing the current time and date, retrieving information from Wikipedia, telling jokes, and more.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- pywhatkit
- speech_recognition
- pyttsx3
- wikipedia
- pyjokes

You can install these dependencies using pip:

```bash
pip install pywhatkit speechrecognition pyttsx3 wikipedia pyjokes
```

## Usage

To use the virtual assistant, follow these steps:

1. Run the Python script using the command:

   ```bash
   python virtual_assistant.py
   ```

2. Once the script is running, the virtual assistant will introduce itself and ask for your command.

3. Start speaking your command after the prompt "listening...". You can start your command with the word "Alexa" followed by the action you want to perform.

4. The virtual assistant will process your command and respond accordingly. It can play videos on YouTube, provide the current time and date, retrieve information from Wikipedia, tell jokes, and more.

5. The virtual assistant will also speak the response back to you.

6. You can continue giving commands to the virtual assistant until you stop the script.

## Available Commands

- **Play**: You can ask the virtual assistant to play a video on YouTube by saying "Alexa, play <video name>".

- **Time**: You can ask the virtual assistant for the current time by saying "Alexa, what is the time?".

- **Date**: You can ask the virtual assistant for the current date by saying "Alexa, what is the date today?".

- **Information**: You can ask the virtual assistant for information about a person or a topic by saying "Alexa, who is <person>?" or "Alexa, what is <thing>?".

- **Joke**: You can ask the virtual assistant to tell a joke by saying "Alexa, tell me a joke".

- **Relationship**: You can ask the virtual assistant if it is single by saying "Alexa, are you single?".

Note: Make sure to have an active internet connection for the virtual assistant to work properly.

## License

This project is licensed under the [MIT License](LICENSE).
