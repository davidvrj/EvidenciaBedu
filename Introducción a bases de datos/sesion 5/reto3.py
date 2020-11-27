'''Usando la colección sample_airbnb.listingsAndReviews, mediante el uso de agregaciones, 
encontrar el número de publicaciones que tienen conexión a Internet, sea desde Wifi 
o desde cable (Ethernet).'''


from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://david:davidrojas98@cluster0.kvy67.mongodb.net/test?authSource=admin&replicaSet=atlas-cil4pt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'amenities': {
                '$in': [
                    'Wifi', 'Ethernet'
                ]
            }
        }
    }, {
        '$group': {
            '_id': None, 
            'total': {
                '$sum': 1
            }
        }
    }, {}
])
