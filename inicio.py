from gtts import gTTS
from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def logar():
    return render_template('login.html')

@app.route('/autenticar',methods=['GET','POST'])
def autenticar():
    if request.method == 'POST':
        if request.form['senha'] == '123' and request.form['usuario'] == 'Joao':
            return render_template('senia.html')
        else:
            msg = 'Erro na autenticação'
            return render_template('login.html',msg=msg)

@app.route('/senia',methods=['GET','POST'])
def abrir_assistente():
    audio_path = None
    if request.method == 'POST':
        texto = request.form['texto']
        lingua = 'pt-br'

        tts = gTTS(text=texto, lang=lingua, tld='com.br')

        audio_path = "static/audio_exemplo.mp3"

        tts.save(audio_path)
    return render_template('senia.html', audio_path=audio_path)
    
if __name__ == '__main__':
    app.run(debug=True)