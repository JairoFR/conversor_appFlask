import os
import re
from flask import flash
from flask_conversor.config.mysqlconnection import connectToMySQL
from flask_conversor.models.base_modelo import BaseModelo


class Audios(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'audios' #nombre de tabla
    columnas_tabla = ['id_usuario', 'audio'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id_conversion = data['id_conversion']
        self.id_usuario = data['id_usuario']
        self.archivo = data['audio']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def ultimo_audio(cls, data): 

        query = f"SELECT * FROM {cls.modelo} where audios.id_usuario = %(data)s ORDER by id_conversion DESC LIMIT 1;"
        data = { 'data': data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) < 1:
            return False
        return results

    @classmethod
    def destroy(cls,data):
        query  = f"DELETE FROM {cls.modelo} WHERE audio = %(data)s;"
        data = { 'data': data}
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)