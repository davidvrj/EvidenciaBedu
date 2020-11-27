'''Usando la colección sample_airbnb.listingsAndReviews, agrega un filtro que permita 
obtener todas las publicaciones que tengan 50 o más comentarios, que la 
valoración sea mayor o igual a 80, que cuenten con conexión a Internet vía
 cable y estén ubicada en Brazil.'''




# Requires the PyMongo package.
# https://api.mongodb.com/python/current


import re
from pymongo import MongoClient
client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'number_of_reviews': {
        '$gte': 50
    }, 
    'review_scores.review_scores_rating': {
        '$gte': 80
    }, 
    'amenities': {
        '$in': [
            re.compile(r"Ethernet")
        ]
    }, 
    'address.country_code': 'BR'
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)


