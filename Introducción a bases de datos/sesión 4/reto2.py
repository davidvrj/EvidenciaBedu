'''Usando la base de datos sample_mflix, agrega proyeccciones, filtros, ordenamientos y l�mites que permitan contestar las siguientes preguntas.

�Qu� comentarios ha hecho Greg Powell?
�Qu� comentarios han hecho Greg Powell o Mercedes Tyler?
�Cu�l es el m�ximo n�mero de comentarios en una pel�cula?
�Cu�l es t�tulo de las cinco pel�culas m�s comentadas?'''
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

from pymongo import MongoClient
#Qu� comentarios ha hecho Greg Powell?
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


#Qu� comentarios han hecho Greg Powell o Mercedes Tyler?

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

#�Cu�l es el m�ximo n�mero de comentarios en una pel�cula?

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

#�Cu�l es t�tulo de las cinco pel�culas m�s comentadas?

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

