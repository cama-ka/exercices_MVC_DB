#datas / gerer les infos
from tinydb import TinyDB, Query


db = TinyDB('test.json')
db.insert({'info':'1'})

print(type(db))