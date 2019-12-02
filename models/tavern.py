import abc

from models.lifestyle import Lifestyle, get_tavern_cost
from models.owner import Owner
from models.menu import Menu


class Tavern:
    def __init__(self):
        self.name = ""
        self.owner = Owner()
        self.description = ""
        self.clientele = ""
        self.costPerNight = ""
        self.menu = Menu()
        self.lifestyle = Lifestyle.SQUALID
        self.cost = ""

    def __str__(self):
        return "{} -- {}\nOwned by {}\nMenu: {}\nClientele: {}\nCost per night: {}"\
            .format(
                self.name,
                self.description,
                self.owner,
                self.menu,
                self.clientele,
                self.get_cost()
            )

    def get_cost(self):
        if self.cost == "":
            self.cost = get_tavern_cost(self.lifestyle)
            return self.cost
        else:
            return self.costcost
