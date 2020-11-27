'''Usando la base de datos sample_airbnblistingsAndReviews, realiza los siguientes filtros:

Propiedades que no permitan fiestas.
Propiedades que admitan mascotas.
Propiedades que no permitan fumadores.
Propiedades que no permitan fiestas ni fumadores.'''

import re
from pymongo import MongoClient

#Propiedades que no permitan fiestas.
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"No Parties(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Propiedades que admitan mascotas.
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"Pets Allowed(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Propiedades que no permitan fumadores.

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"No Smoking(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Propiedades que no permitan fiestas ni fumadores.
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"No Smoking|No Parties(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)