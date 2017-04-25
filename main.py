from char import Char
from tinydb import TinyDB, Query
import json


class Game:
    def __init__(self):
        self.db = TinyDB('db/database.json')
        # char_table = db.table('character')
        self.welcome()

    def welcome(self):
        name = raw_input("Please, enter your name ")

        char = Char(name)
        result = char.search(name)

        if len(result) == 0:
            char.save_to_db()
            print("Looks like it is your first time here, {}".format(name))
        else:
            print("Welcome back, {}".format(name))
            # char.set(result)

            # char.print_status()


Game()
