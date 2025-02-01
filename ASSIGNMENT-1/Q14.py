print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")
import random
from dataclasses import dataclass
@dataclass
class Card:
    rank: str
    suit: str
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)
    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards left in the deck!")
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return hand
deck = Deck()
player_hand = deck.deal(5)
print("Player's Hand:")
for card in player_hand:
    print(f"{card.rank} of {card.suit}")
print(f"Remaining Cards in Deck: {len(deck.cards)}\n")
print("\nExplanation: The Card data class represents a playing card with a rank and suit.\n")
print("Explanation: The Deck class initializes a standard deck, shuffles it, and includes a deal() method to distribute cards.\n")
print("Explanation: The deal() method returns a specified number of cards to the player while updating the deck.\n")
print("Explanation: This simulation showcases object-oriented principles and randomness to emulate a real card game scenario.\n")
