class Board(object):
    def __init__(self, num_players):
        self.num_players = num_players
        self.liberal_board = []
        self.fascist_board = []
        self.fascist_actions = []

        if self.num_players == 5 or self.num_players == 6:
            self.fascist_actions = [None, None, "Examine", "Kill", "Kill", None]
        if self.num_players == 7 or self.num_players == 8:
            self.fascist_actions = [None, "Investigate", "Pick", "Kill", "Kill", None]
        if self.num_players == (9 or 10):
            self.fascist_actions = ["Investigate", "Investigate", "Pick", "Kill", "Kill", None]

    def play_lib_policy(self):
        self.liberal_board.append("Liberal")

    def display_lib_board(self):
        display = [None, None, None, None, None]
        for i, card in enumerate(self.liberal_board):
            display[i] = card
        print(display)

    def play_fascist_policy(self):
        self.fascist_board.append("Fascist")

    def display_fascist_board(self):
        display = self.fascist_actions
        for i, card in enumerate(self.fascist_board):
            display[i] = card
        print(display)

    def play_policy(self, card):
        if card == "Liberal":
            self.play_lib_policy()
            return None
        else:
            self.play_fascist_policy()
            fascist_index = len(self.fascist_board) - 1
            return self.fascist_actions[fascist_index]











