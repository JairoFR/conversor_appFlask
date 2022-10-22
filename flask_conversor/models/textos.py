import os
import re
from flask import flash
from flask_conversor.config.mysqlconnection import connectToMySQL
from flask_conversor.models.base_modelo import BaseModelo


class Texto(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'textos' #nombre de tabla
    columnas_tabla = ['id_usuario', 'texto'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id_textos = data['id_textos']
        self.id_usuario = data['id_usuario']
        self.texto = data['texto']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def ultimo_audio(cls, data): 

        query = f"SELECT * FROM {cls.modelo} where conversiones.id_usuario = %(data)s ORDER by id_conversion DESC LIMIT 1;"
        data = { 'data': data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) < 1:
            return False
        return results

