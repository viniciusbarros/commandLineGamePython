from char import Char
from tinydb import TinyDB, Query
from useful import ColourPrint
from useful import GenericMenu
import os
import json


class Game:
    logged_in = False
    menu_options = {
        'login': 'Do login',
        'quit': 'Quit game'
    }
    char = None

    def __init__(self):
        self.db = TinyDB('db/database.json')

        #Game Loop
        while True:
            if self.char is None or self.char.logged_in is False:
                os.system('clear')
                GenericMenu.generic_menu("Main Menu", "What do you want to do?", self.menu_options, self)
            else:

                GenericMenu.generic_menu("Char Menu", "What do you want to do?", self.char.char_menu, self.char)


    def login(self):
        os.system('clear')
        ColourPrint.print_line("Login")
        name = raw_input("Please, enter your name: ")

        self.char = Char(name)
        result = self.char.search(name)

        if len(result) == 0:
            self.char.save_to_db()
            print("Welcome {0}! Looks like it is your first time here.".format(name))
        else:
            self.char.set(result[0])
            print("Welcome back, {}".format(name))
            # char.level_up()
            # char.save_to_db()

        self.char.logged_in = True

    def quit(self):
        ColourPrint.print_blue("Bye Bye")
        quit()

Game()
