'''Usando la base de datos sample_mflix, agrega proyeccciones, filtros, ordenamientos y límites que permitan contestar las siguientes preguntas.

¿Qué comentarios ha hecho Greg Powell?
¿Qué comentarios han hecho Greg Powell o Mercedes Tyler?
¿Cuál es el máximo número de comentarios en una película?
¿Cuál es título de las cinco películas más comentadas?'''
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

from pymongo import MongoClient
#Qué comentarios ha hecho Greg Powell?
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'name': 'Greg Powell'
}
project={
    'name': 1, 
    'text': 1
}

result = client['sample_mflix']['comments'].find(
  filter=filter,
  projection=project
)


#Qué comentarios han hecho Greg Powell o Mercedes Tyler?

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    '$or': [
        {
            'name': 'Greg Powell'
        }, {
            'name': 'Mercedes Tyler'
        }
    ]
}
project={
    'name': 1, 
    'text': 1
}

result = client['sample_mflix']['comments'].find(
  filter=filter,
  projection=project
)

#¿Cuál es el máximo número de comentarios en una película?

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'num_mflix_comments': 1
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=1

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

#¿Cuál es título de las cinco películas más comentadas?

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=5

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

