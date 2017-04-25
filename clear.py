from tinydb import TinyDB, Query

db = TinyDB('db/database.json')
db.purge()
