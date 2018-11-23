from Player import Player
from Gameboard import Board
import SH_Roles
import random
from Deck import Deck


class GameState(object):
    # Contains all game characteristics
    def __init__(self, num_players, player_names):
        self.num_players = num_players
        self.players = []
        self.player_names = player_names
        self.current_pres = None
        self.current_chanc = None
        self.previous_chanc = None
        self.previous_pres = None
        self.hitler = None
        self.votes = []
        self.board = None
        self.deck = None
        self.alive_players = num_players

    def setup(self):

        # Assign Roles
        num_fascists = 0
        if self.num_players in [5, 6]:
            num_fascists = 1
        if self.num_players in [7, 8]:
            num_fascists = 2
        if self.num_players in [9, 10]:
            num_fascists = 3
        num_liberals = self.num_players - num_fascists - 1
        player_roles = [SH_Roles.Liberal()] * num_liberals + \
        [SH_Roles.Fascist()] * num_fascists + \
        [SH_Roles.Hitler()]

        random.shuffle(player_roles)

        for i in range(self.num_players):
            player = Player(self.player_names[i], player_roles[i])
            self.players.append(player)

            if player.is_Hitler():
                self.hitler = player

        # Setup Board & Deck
        self.board = Board(self.num_players)
        self.deck = Deck()
        self.deck.shuffle()

        # Pick first president
        self.current_pres = self.players[random.randint(0, self.num_players - 1)]


