print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck shuffled.")
    
    def deal(self, num_cards):
        hand = []
        for _ in range(num_cards):
            hand.append(self.cards.pop())
        return hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def receive_cards(self, cards):
        self.hand.extend(cards)
    
    def show_hand(self):
        print(f"{self.name}'s Hand: ", ', '.join(str(card) for card in self.hand))

deck = Deck()
deck.shuffle()

player1 = Player("Player 1")
player2 = Player("Player 2")

player1.receive_cards(deck.deal(5))
player2.receive_cards(deck.deal(5))

player1.show_hand()
player2.show_hand()
