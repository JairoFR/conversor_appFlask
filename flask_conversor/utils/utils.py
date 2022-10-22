# acá dejaremos las funciones comunes
from flask_conversor import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS