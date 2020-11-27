#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usando las colecciones comments y users, se requiere conocer el correo y contraseña de
 cada persona que realizó un comentario. Construye un pipeline que genere como
 resultado estos datos.

"""
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_mflix']['comments'].aggregate([
    {
        '$lookup': {
            'from': 'users', 
            'localField': 'name', 
            'foreignField': 'name', 
            'as': 'usuario'
        }
    }, {
        '$addFields': {
            'usuario_objeto': {
                '$arrayElemAt': [
                    '$usuario', 0
                ]
            }
        }
    }, {
        '$addFields': {
            'usuario_password': '$usuario_objeto.password'
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'email': 1, 
            'usuario_password': 1
        }
    }
])


