import random

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1)+ binomial_coefficient(n-1, k)


def hypergeometric_distribution(pop_size, tot_success, num_draws, obs_success):
    return (binomial_coefficient(tot_success, obs_success)
            * binomial_coefficient(pop_size-tot_success, num_draws-obs_success)) \
           / binomial_coefficient(pop_size, num_draws)


def prob_of_num_libs(num_libs, liberals_face_up = 0, fascists_face_up = 0):
    L = 6 - liberals_face_up
    F = 11 - fascists_face_up

    return hypergeometric_distribution(L + F, L, 3, num_libs)


class Deck(object):
    def __init__(self):
        self.list = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.discard_list = []

    def shuffle(self):
        random.shuffle(self.list)

    def check_draw_pile(self):
        if len(self.list) < 3:
            for cards in self.discard_list:
                self.list.append(cards)
                self.discard_list.pop(0)
            self.shuffle()


class InHand(object):
    card_key = ["Fascist", "Liberal"]

    def __init__(self):
        self.inHand = [1, 0, 1]
        super().__init__()

    def __str__(self):
        result = "You have the following cards: \n"
        for counter, card in enumerate(self.inHand, 1):
            result += (str(counter)) + ". " + self.card_key[card] + " "
        return result


hand = InHand()


class Player(object):

    def __init__(self, name, liberal, role=False):
        self.name = name
        self.liberal = liberal
        self.alive = True
        self.role = role
        self.pres_record = [[], []]
        self.chanc_record = [[], []]
        self.next = None
        super().__init__()

    def pres_action(self, claimed_discard, num_libs):
        self.pres_record[0].append(num_libs)
        self.pres_record[1].append(claimed_discard)

    def chanc_action(self, num_libs, played):
        self.chanc_record[0].append(num_libs)
        self.chanc_record[1].append(played)

player1 = Player("John", True)
player2 = Player("Bob", True)
player3 = Player("Mary", False)
player4 = Player("Susan", True)
player5 = Player("Jim", False, True)

player1.next = player2
player2.next = player3
player3.next = player4
player4.next = player5
player5.next = player1


class Action(InHand, Deck, Player):
    current_pres = player1
    current_chanc = player2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#    def choose_card(self, list_cards):
#        print ('You have the following cards: ')
#        for i in range(len(list_cards)):

    def turn(self):
        self.check_draw_pile()
        for i in range(3):
            self.inHand.append(self.list.pop(0))
        print(hand)
        selection = input("Enter 1,2, or 3 to select a card to discard")
        self.discard_list.append(self.inHand.pop(selection - 1))

        print(hand)
        selection = input("Enter 1 or 2 to select a card to discard")
        self.discard_list.append(self.inHand.pop(selection - 1))

        print("This card was played: ", self.inHand)













