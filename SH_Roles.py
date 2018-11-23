class Role(object):
    def __init__(self):
        self.party = ""
        self.role = ""


class Liberal(Role):
    def __init__(self):
        super().__init__()
        self.party = "Liberal"
        self.role = None


class Fascist(Role):
    def __init__(self):
        super().__init__()
        self.party = "Fascist"
        self.role = None


class Hitler(Role):
    def __init__(self):
        super().__init__()
        self.party = "Fascist"
        self.role = "Hitler"
