class Player(object):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.dead = False

    def is_fascist(self):
        return self.role.party == "Fascist"

    def is_Hitler(self):
        return self.role.role == "Hitler"

    def killed(self):
        self.dead = True

    def __str__(self):
        return self.name

