import random


class Deck(object):
    def __init__(self):
        self.cards = ["Liberal", "Liberal", "Liberal", "Liberal", "Liberal", "Liberal",
                      "Fascist", "Fascist", "Fascist", "Fascist", "Fascist", "Fascist",
                      "Fascist", "Fascist", "Fascist", "Fascist", "Fascist"]
        self.discard = []

    def shuffle(self):
        random.shuffle(self.cards)

    def pickup3(self):
        hand = []
        for i in range(3):
            hand.append(self.cards.pop(0))
        return hand

    def get_top_card(self):
        return self.cards.pop(0)

    def discard_card(self, card):
        self.discard.append(card)

    def reshuffle(self):
        if len(self.cards) < 3:
            for card in self.discard:
                self.cards.append(self.discard.pop(0))
            self.shuffle()

