from tinydb import TinyDB, Query
from useful import ColourPrint


class Char:
    name = None
    hp = None
    attack = None
    defense = None
    lucky = None
    level = None
    points = None
    logged_in = False

    char_menu = {
        'status': 'Check all your status',
        'points': 'Use points',
        'logoff': 'Press enter to leave menu'
    }

    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.attack = 1
        self.defense = 1
        self.lucky = 0.05
        self.level = 1
        self.points = 5
        self.db = TinyDB('db/database.json')

    def suffer_attack(self, attack):
        if attack > self.defense:
            self.hp -= attack - self.defense
            if self.hp < 0:
                self.hp = 0

    def is_alive(self):
        status = self.hp > 0
        if status:
            print("{} is alive!".format(self.name))
        else:
            print("{} is dead :( !".format(self.name))
        return self.hp > 0

    def print_status(self):
        print(self.get())

    def get(self):
        data = {
            'name': self.name,
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'lucky': self.lucky,
            'level': self.level,
            'points': self.points
        }
        return data

    def set(self, data):
        self.name = data['name']
        self.hp = data['hp']
        self.attack = data['attack']
        self.defense = data['defense']
        self.lucky = data['lucky']
        self.level = data['level']
        self.points = data['points']

    def level_up(self):
        self.level += 1
        if self.level % 2:
            self.points += 2
        else:
            self.points += 1

    def search(self, name):
        query = Query()
        search = self.db.search(query.name == self.name)
        return search

    def save_to_db(self):
        search = self.search(self.name)
        if len(search) == 0:
            self.db.insert(self.get())
        else:
            query = Query()
            self.db.update(self.get(), query.name == self.name)

    def status(self):
        ColourPrint.print_line("{} Status".format(self.name))
        print(ColourPrint.get_blue("Name: ") + ColourPrint.get_green(self.name))
        print(ColourPrint.get_blue("Level: ") + ColourPrint.get_green(str(self.level)))
        print(ColourPrint.get_blue("HP: ") + ColourPrint.get_green(str(self.hp)))
        print(ColourPrint.get_blue("Attack: ") + ColourPrint.get_green(str(self.attack)))
        print(ColourPrint.get_blue("Defense: ") + ColourPrint.get_green(str(self.defense)))
        print(ColourPrint.get_blue("Lucky: ") + ColourPrint.get_green(str(self.lucky)))
        print(ColourPrint.get_blue("Points: ") + ColourPrint.get_green(str(self.points)))

    # def points(self):
    #     ColourPrint.print_line("{} Points".format(self.name))
    #     if self.points <= 0:
    #         ColourPrint.print_red("You have 0 enough points to use. Go training more and come back later")
    #     else:
    #         ColourPrint.print_blue("You have {} points.")

    def logoff(self):
        self.logged_in = False