import os
from flask_conversor import app
from flask import redirect, render_template, request, flash, session, url_for
from flask_conversor.models.usuario import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if 'usuario' in session:
        flash('Cierra session para salir', 'error')
        return redirect('/conversor')
    return render_template("index.html")



@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == 'GET':
        return render_template('/login/signup.html')

    if request.method == 'POST':

        dato = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['password'],
            'cpassword': request.form['cpassword'],
        }

        if not Usuario.validar_signup(dato):
            
            return redirect('/signup')

        pass_hash = bcrypt.generate_password_hash(request.form['password'])

        data = {
            'username' : request.form['username'],
            'email' : request.form['email'],
            'password' : pass_hash,
        }

        resultado = Usuario.save(data)

        if not resultado:
            flash("error al crear el usuario", "error")
            return redirect("/signup")

        flash("Usuario creado correctamente", "success")
        return redirect("/login")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "GET":
        return render_template("/login/login.html")

    if request.method == "POST":

        usuario = Usuario.buscar(request.form['email'])
        print('impriemiendo usuario', usuario)
        if not usuario:
            flash("Usuario/Correo/Clave Invalidas", "error")
            return redirect("/login")

        if not bcrypt.check_password_hash(usuario.password, request.form['password']):
            flash("Usuario/Correo/Clave Invalidas", "error")
            return redirect("/login")

        session['usuario'] = usuario.username
        session['usuario_id'] = usuario.id_usuario

        return redirect(url_for('principal'))

@app.route('/logout')
def logout():
    
    session.clear()
    return redirect('/login')