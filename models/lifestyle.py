from enum import Enum


class Lifestyle(Enum):
    SQUALID = 1,
    POOR = 2,
    MODEST = 3,
    COMFORTABLE = 4,
    WEALTHY = 5,
    ARISTOCRATIC = 6


def get_tavern_cost(lifestyle):
    if lifestyle == Lifestyle.SQUALID:
        return "7 cp"
    elif lifestyle == Lifestyle.POOR:
        return "1 sp"
    elif lifestyle == Lifestyle.MODEST:
        return "5 sp"
    elif lifestyle == Lifestyle.COMFORTABLE:
        return "8 sp"
    elif lifestyle == Lifestyle.WEALTHY:
        return "2 gp"
    elif lifestyle == Lifestyle.ARISTOCRATIC:
        return "4 gp"


def get_meal_cost(lifestyle):
    if lifestyle == Lifestyle.SQUALID:
        return "3 cp"
    elif lifestyle == Lifestyle.POOR:
        return "6 cp"
    elif lifestyle == Lifestyle.MODEST:
        return "3 sp"
    elif lifestyle == Lifestyle.COMFORTABLE:
        return "5 sp"
    elif lifestyle == Lifestyle.WEALTHY:
        return "8 sp"
    elif lifestyle == Lifestyle.ARISTOCRATIC:
        return "2 gp"
