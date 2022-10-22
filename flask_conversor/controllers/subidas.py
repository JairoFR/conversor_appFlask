import os
from flask_conversor import app
from flask import render_template,redirect,request,session,flash,url_for
from flask_conversor.models.usuario import Usuario
from flask_conversor.models.audios import Audios
from flask_conversor.models.textos import Texto
from flask_conversor.utils.utils import allowed_file
from werkzeug.utils import secure_filename
from flask import send_file
from flask_conversor.conversion import save_transcription, upload, archivo_ruta


#aca en el controlador se ingresan las rutas
@app.route('/conversor')
def principal():

    return render_template("logueado.html")

@app.route('/conversor/audio', methods=['POST'])
def upload_audio():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part','error')
            return redirect(url_for('add_songs'))
        file = request.files['file']
      
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(url_for('add_songs'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {
                'audio': filename,
                'id_usuario': session['usuario_id']
            }

            Audios.save(data)
            return redirect(url_for('convertir_audio')) 

@app.route('/conversor/audio/api', methods=['POST', 'GET'])
def convertir_audio():

    if request.method == 'GET':
        audio = Audios.ultimo_audio(session['usuario_id'])
        print('audio',audio)
        return render_template('/convertir_audio.html', audio=audio)

    if request.method == 'POST':
        file = request.form['filename']
        filename = archivo_ruta(file)
        audio_url = upload(filename)
        nombre = save_transcription(audio_url, request.form['filename'])
        data = {
                'texto': nombre,
                'id_usuario': session['usuario_id']
            }
        Texto.save(data)
        os.remove(f'flask_conversor\\static\\uploads\\{file}') #borra el archivo de audio
        return redirect(url_for('downloadFile', name=nombre)) 

@app.route('/download/<name>')
def downloadFile (name):
  
    path = f'..\\flask_conversor\\static\\uploads\\{name}'
    return send_file(path, as_attachment=True)




