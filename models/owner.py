class Owner:
    def __init__(self):
        self.name = ""
        self.description = ""

    def __str__(self):
        return "{} -- {}".format(self.name, self.description)