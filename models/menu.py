from models.lifestyle import Lifestyle, get_meal_cost


class Menu:
    def __init__(self):
        self.breakfast = ""
        self.lunch = ""
        self.dinner = ""
        self.lifestyle = Lifestyle.SQUALID

    def __str__(self):
        return "For {}, you get {} for breakfast, {} for lunch, and {} for dinner"\
            .format(
                self.get_cost(),
                self.breakfast,
                self.lunch,
                self.dinner
            )

    def get_cost(self):
        return get_meal_cost(self.lifestyle)
