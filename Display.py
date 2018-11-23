class Display(object):
    def __init__(self):
        pass

    def get_choice(self, players):
        choice = 0
        for index, player in enumerate(players):
            print("{}. {}".format(index + 1, player))
        while choice not in range(1, len(players) + 1):
            try:
                choice = int(input("Enter one of the above numbers: "))
            except ValueError:
                choice = 0
        choice -= 1
        return choice

    def get_num_players(self):
        result = 0
        while result not in range(5, 11):
            try:
                result = int(input("Enter number of players: "))
            except ValueError:
                result = 0
        return result
    def get_player_names(self, num_players):
        player_names = []
        for i in range(num_players):
            name = input("Enter Player {}'s name: ".format(i + 1))
            player_names.append(name)
        return player_names

    def get_votes(self, voters):
        vote_total = 0
        for voter in voters:
            vote = None
            while vote not in ["j", "n"]:
                vote = input("{}, enter [J]a or [N]ein to cast your vote: ".format(voter)).lower()
            if vote == "j":
                vote_total += 1
            if vote == "n":
                vote_total -= 1
        return vote_total

    def choose_discard(self, cards):
        for i, card in enumerate(cards):
            print("{}. {}".format(i+1, card), end=" ")
        result = 0
        while result not in range(1, len(cards) + 1):
            try:
                result = int(input("\nSelect one to remove: "))
            except ValueError:
                result = 0
        result -= 1
        return result

    def veto_or_discard(self, cards):
        for i, card in enumerate(cards):
            print("{}. {}".format(i+1, card), end=" ")
        result = 0
        while result not in range(1, len(cards) + 2):
            try:
                result = int(input("\nSelect one to remove, or enter 3 to veto: "))
            except ValueError:
                result = 0
        if result == 3:
            veto = input("Do you accept this veto?[y/n]")
            if veto.lower() == "y":
                return "Veto"
            else:
                # Repeat request if veto is declined
                for i, card in enumerate(cards):
                    print("{}. {}".format(i+1, card), end=" ")
                result = 0
                while result not in range(1, len(cards) + 1):
                    try:
                        result = int(input("\nSelect one to remove: "))
                    except ValueError:
                        result = 0
        result -= 1
        return result

    def player_roles(self, players):
        for player in players:
            print("{} is {}".format(player, player.role.party))
            if player.is_Hitler():
                print(" and Hitler")


