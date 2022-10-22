from os.path import join
from flask import Flask
import os
    

carpeta = 'static\\uploads'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = join(BASEDIR, carpeta)
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ.get("APP_SECRET_KEY")




