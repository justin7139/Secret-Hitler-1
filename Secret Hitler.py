import GameState
from Player import Player
from Gameboard import Board
import SH_Roles
import random
from Display import Display


class SecretHitler(object):
    def __init__(self):
        self.num_players = 0
        self.player_names = []
        self.display = None
        self.state = None

    def game(self):
        self.display = Display()

        # Get number of players & player names
        self.num_players = self.display.get_num_players()
        self.player_names = self.display.get_player_names(self.num_players)

        self.state = GameState.GameState(self.num_players, self.player_names)
        self.state.setup()

        while not self.test_for_victory():
            self.next_president()
            self.choose_chanc()

            num_failed_votes = 0
            while not self.vote():
                num_failed_votes += 1
                if num_failed_votes == 3:
                    print("You have failed to elect a party, now the top card is played")
                    self.state.board.play_policy(self.state.deck.get_top_card())
                    num_failed_votes = 0
                    break
                self.next_president()
                self.choose_chanc()

            if self.test_for_victory():
                break

            action = self.take_turn()

            print("Liberal Board:")
            self.state.board.display_lib_board()
            print("Fascist Board")
            self.state.board.display_fascist_board()

            self.check_action(action)

        print(self.test_for_victory())

    def choose_chanc(self):
        # Choose chancellor
        valid_choices = []
        for person in self.state.players:
            if person.dead is False and person != self.state.previous_chanc and person != self.state.current_pres and (
                person != self.state.previous_pres or self.state.alive_players < 6
            ):
                valid_choices.append(person)
            else:
                continue
        print("{}, choose one of the following to be chancellor".format(self.state.current_pres))
        # print("These are the valid choices: {}".format(valid_choices))
        self.state.current_chanc = valid_choices[self.display.get_choice(valid_choices)]
        print("{} has been chosen as chancellor".format(self.state.current_chanc))

    def vote(self):
        print("We are voting on {} as president and {} as chancellor".format(self.state.current_pres,
                                                                             self.state.current_chanc))
        valid_voters = []
        for person in self.state.players:
            if person.dead is False:
                valid_voters.append(person)

        vote_result = self.display.get_votes(valid_voters)

        if vote_result > 0:
            print("The vote has passed!")
            self.state.previous_chanc = self.state.current_chanc
            self.state.previous_pres = self.state.current_pres
            return True
        else:
            print("The vote has not passed")
            return False

    def next_president(self):
        pres_index = self.state.players.index(self.state.current_pres)
        if pres_index == len(self.state.players) - 1:
            pres_index = 0
        else:
            pres_index += 1

        while self.state.players[pres_index].dead:
            if pres_index == len(self.state.players) - 1:
                pres_index = 0
            else:
                pres_index += 1

        self.state.current_pres = self.state.players[pres_index]

    def take_turn(self):
        inhand = self.state.deck.pickup3()

        print("{} ,you have the following cards: ".format(self.state.current_pres.name))
        input("Press ENTER to continue...")
        discard_index = self.display.choose_discard(inhand)
        self.state.deck.discard_card(inhand.pop(discard_index))

        print("{} ,you have the following cards: ".format(self.state.current_chanc.name))
        input("Press ENTER to continue...")
        discard_index = self.display.choose_discard(inhand)
        self.state.deck.discard_card(inhand.pop(discard_index))

        self.state.deck.reshuffle()

        return self.state.board.play_policy(inhand[0])

    def check_action(self, action):

        if action == "Examine":
            self.examine()
        elif action == "Investigate":
            self.investigate()
        elif action == "Pick":
            self.pick()
        elif action == "Kill":
            self.kill()

    def examine(self):
        to_examine = []
        for i in range(3):
            to_examine.append(self.state.deck.cards[i])
        input("{}, press any key to examine the top 3 cards".format(self.state.current_pres))
        print("The top three cards are:")
        for i, card in enumerate(to_examine):
            print("{}. {}".format(i + 1, card), end=" ")
        input("Press ENTER to continue...")

    def investigate(self):
        valid_choices = []
        for player in self.state.players:
            if player != self.state.current_pres:
                valid_choices.append(player)
        print("Choose a player to investigate: ")
        index = self.state.get_choice(valid_choices)
        print("This player's party is {}".format(self.state.valid_choices[index].role.party))

    def pick(self):
        valid_choices = []
        for player in self.state.players:
            if player != self.state.current_pres:
                valid_choices.append(player)
        print("Choose a player to make next president: ")
        index = self.state.get_choice(valid_choices)
        self.state.current_pres = valid_choices[index]
        print("{} is the new president".format(self.state.current_pres))

    def kill(self):
        valid_choices = []
        for player in self.state.players:
            if player != self.state.current_pres and not player.dead:
                valid_choices.append(player)
        print("Choose a player to kill: ")
        index = self.display.get_choice(valid_choices)
        valid_choices[index].killed()
        print("{} is now dead".format(valid_choices[index]))
        return valid_choices[index].is_Hitler()

    def test_for_victory(self):
        # If Hitler elected chancellor
        if len(self.state.board.fascist_board) >= 3 and self.state.current_chanc == self.state.hitler:
            return "Hitler has been elected chancellor, Fascists win!"

        # If Fascist board fills up
        if len(self.state.board.fascist_board) == 6:
            return "Fascists win by passing policy!"

        # If Hitler is killed
        for player in self.state.players:
            if player.dead and player.is_Hitler():
                return "Hitler has been killed, Liberals win!"

        # If Liberal board fills up
        if len(self.state.board.liberal_board) == 5:
            return "Liberals win by passing policy!"

        return None









s = SecretHitler()
s.game()

