from models.lifestyle import Lifestyle
from models.owner import Owner
from models.tavern import Tavern
from models.menu import Menu


def get_taverns():
    menu = Menu()
    menu.breakfast = "poached eggs and potatoes and cup of fruit"
    menu.lunch = "chicken noodle soup"
    menu.dinner = "steak and green beans"
    menu.lifestyle = Lifestyle.WEALTHY
    owner = Owner()
    owner.name = "Gentlemen Johnny"
    owner.description = "A well dressed copper dragonborn full of mirth"
    tavern = Tavern()
    tavern.name = "Countryside Palace"
    tavern.clientele = "A single young man sipping a cup of tea."
    tavern.description = "A victorian style house with a cozy hearth and colorful fabrics"
    tavern.lifestyle = Lifestyle.WEALTHY
    tavern.menu = menu
    tavern.owner = owner
    tavern_list = list()
    tavern_list.append(tavern)
    return tavern_list
