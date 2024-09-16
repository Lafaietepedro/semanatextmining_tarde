from gtts import gTTS
from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    audio_path = None
    if request.method == 'POST':
        texto = request.form['texto']
        lingua = 'pt-br'

        tts = gTTS(text=texto, lang=lingua, tld='com.br')

        audio_path = "static/audio_exemplo.mp3"

        tts.save(audio_path)
    return render_template('index.html', audio_path=audio_path)
    
if __name__ == '__main__':
    app.run(debug=True)