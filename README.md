# Jarvis Virtual Assistant

## Overview

Jarvis is a voice-activated virtual assistant built using Python. It leverages various libraries to perform tasks such as playing music, providing time and date information, answering questions, and retrieving information from Wikipedia.

## Features

- **Voice Recognition**: Listens for user commands using the `speech_recognition` library.
- **Text-to-Speech**: Responds to user commands with spoken feedback using `pyttsx3`.
- **Music Playback**: Plays songs from YouTube using `pywhatkit`.
- **Date and Time Information**: Provides current date and time on request.
- **Information Retrieval**: Fetches summaries from Wikipedia based on user queries.

## Requirements

To run this assistant, you need to have the following libraries installed:

- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`

You can install these libraries using pip:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
```

## Getting Started

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/Mansiiiiiiiiiiiiiiiii/Virtual-Assistant.git
   cd Virtual-Assistant
   ```

2. **Run the Assistant**:
   Make sure your microphone is set up and then run the script:
   ```bash
   python jarvis.py
   ```

3. **Usage**:
   - Start the conversation by saying "Jarvis" followed by your command.
   - Example commands:
     - "Jarvis, play baari"
     - "Jarvis, what time is it?"
     - "Jarvis, who is ratan tata?"

## Customization

You can customize the assistant's behavior by modifying the conditions in the `play_jarvis` function. Add more commands or change responses to suit your preferences.

## Troubleshooting

- Ensure your microphone is properly configured.
- If the assistant does not respond, check for errors in the console and ensure all required libraries are installed.

## Contributing

Feel free to fork the repository and submit pull requests for improvements. Any contributions are welcome!
