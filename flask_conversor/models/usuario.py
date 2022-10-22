import os
import re
from flask import flash
from flask_conversor.config.mysqlconnection import connectToMySQL
from flask_conversor.models.base_modelo import BaseModelo

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Usuario(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'usuarios' #nombre de tabla
    columnas_tabla = ['username', 'email', 'password'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id_usuario = data['id_usuario']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validar_signup(data): 
        is_valid = True

        query = "SELECT * FROM usuarios WHERE email = %(data)s;"
        dato = {'data': data['email']}
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,dato) 

        if len(results) >= 1:
            flash("Email ya existe.","error")
            is_valid=False
        
        if len(data['username']) <= 3:
            flash(f'El Usuario no puede ser menor a 3', 'error')
            is_valid = False

        if not EMAIL_REGEX.match(data['email']): 
            flash("Direccion de email invalida!","error")
            is_valid = False

        if len(data['password']) < 8:
            is_valid = False
            flash("La contraseña debe tener minimo de 8 caracteres", 'error')

        if data['password'] != data['cpassword']:
            is_valid = False
            flash("Las contraseñas no coinciden!","error")
        return is_valid
    
    @classmethod
    def buscar(cls, data): 

        query = "SELECT * FROM usuarios WHERE email = %(data)s;"
        data = { 'data': data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data) 
        if len(results) < 1:
            return False
        return cls(results[0])
    