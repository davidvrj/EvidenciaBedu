from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

'''Usando la base de datos sample_mflix, proyecta los datos que se solicitan.

Fecha, nombre y texto de cada comentario.
Título, elenco y año de cada película.
Nombre y contraseña de cada usuario.'''

#Fecha, nombre y texto de cada comentario.
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'date': 1, 
    'name': 1, 
    'text': 1
}

result = client['sample_mflix']['comments'].find(
  filter=filter,
  projection=project
)


#Título, elenco y año de cada película.
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1, 
    'cast': 1, 
    'year': 1
}

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project
)

#Nombre y contraseña de cada usuario

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'name': 1, 
    'password': 1
}

result = client['sample_mflix']['users'].find(
  filter=filter,
  projection=project
)