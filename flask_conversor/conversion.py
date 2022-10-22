import os
import requests
import time
from os.path import join
from flask_conversor import app

#uploads

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': '63ad03b4682c4d4791e9352d8793316c'}


#RUTA DEL ARCHIVO
def archivo_ruta(file):
    file = file
    carpeta = 'static\\uploads'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    filename = join(BASEDIR, carpeta, file)
    return filename


def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))
    #url que llega de la respuesta
    audio_url = upload_response.json()['upload_url']
    return audio_url

#transcribe
def transcribe(audio_url):
    transcribe_request = { "audio_url": audio_url,
                            "language_code": "es" }
    transcipt_response = requests.post(transcript_endpoint, 
                            json=transcribe_request, 
                            headers=headers)
    job_id = transcipt_response.json()['id']
    return job_id



# poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url):
    transcript_id =transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print('Esperando 30 segundos...')
        time.sleep(30)


def save_transcription(audio_url, title):
    data, error = get_transcription_result_url(audio_url)
    
    if data:

        directory = 'flask_conversor\\static\\uploads'
        text_filename = title + '.txt'
        file_path = os.path.join(directory,  text_filename)
        with open(file_path, "w") as f:
            f.write(data['text'])
            print(file_path)#nombre del archivo guardado en el disco f
        print('Transcription saved!!')

    elif error:
        print("error", error)

    return text_filename

