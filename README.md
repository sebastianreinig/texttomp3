# texttomp3 with OpenAI

<img width="40%" alt="Bildschirmfoto 2024-10-20 um 16 45 57" src="https://github.com/user-attachments/assets/1fa0b759-c155-4db6-8ed2-3c5b4ad40de0">


## Overview

`texttomp3` is a simple web-based tool that converts text to mpe3 using OpenAI's  API. The application is built with Flask and Python, providing an easy-to-use interface to transferm text to voice.

Details to the API: https://platform.openai.com/docs/guides/text-to-speech/overview

## Requirements

To run this project, you'll need the following dependencies:

- Flask
- OpenAI API
- Werkzeug

You can install these dependencies using:

```bash
pip install flask openai werkzeug
```

Alternatively, install all required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
To start the application, run the following command:

```bash
python app.py
```

Once the server is running, you can access the web application at http://127.0.0.1:5000.

## Features
Text-to-Audio Conversion: Type in Text and API Key and get an mp3.
Simple Web Interface: Easy-to-navigate interface built with Flask.

## How It Works
1. Type your text and API KEY from OpenAI
2. The file is processed via OpenAI APIs
3. The Voice output is generated as an mp3

Optional: You can change the voice in main.oy

## Demo

currently unavailable


## Credits
This project was coded using Python and OpenAI's ChatGPT for assistance.



