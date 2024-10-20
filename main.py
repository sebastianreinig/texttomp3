from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)
app.config['OUTPUT_FOLDER'] = 'output'
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def generate_audio():
    audio_file_path = None

    if request.method == 'POST':
        # Überprüfung, ob das Formular vollständig ist
        if 'text' not in request.form or 'api_key' not in request.form:
            return 'Es wurde kein Text oder kein API Key übermittelt', 400

        text_input = request.form['text']
        api_key = request.form['api_key']

        if text_input == '' or api_key == '':
            return 'Es wurde kein Text oder kein API Key übermittelt', 400

        # OpenAI API aufrufen
        client = OpenAI(api_key=api_key)

        try:
            # Text-to-Speech-Anfrage
            #possible voices alloy, echo, fable, onyx, nova, and shimmer
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text_input
            )

 
             # Datei speichern
            file_name = 'generated_audio.mp3'
            audio_file_path = os.path.join(app.config['OUTPUT_FOLDER'], file_name)
            with open(audio_file_path, 'wb') as audio_file:
                audio_file.write(response.content)

        except Exception as e:
            return f'Fehler bei der API-Anfrage: {e}', 500

    return render_template('generate.html', audio_file=audio_file_path)

if __name__ == '__main__':
    app.run()
