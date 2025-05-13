import random
import json


with open('cards.json', 'r') as file:
    cards_data = json.load(file)

class Card:
    rank_values = cards_data["ranks"]  


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __repr__(self):
        return f"{self.rank} of {self.suit}"


    def value(self):
        return Card.rank_values[self.rank]


    def __str__(self):
        suit_symbols = {
            "Spades": "\u2660",     # ♠
            "Hearts": "\u2665",     # ♥
            "Diamonds": "\u2666",   # ♦
            "Clubs": "\u2663"       # ♣
        }
        return f"{self.rank} of {suit_symbols[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        for rank in cards_data["ranks"]:
            for suit in cards_data["suits"]:
                self.cards.append(Card(rank, suit))

    def show(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.cards)
        
    def deck_length(self, player):
        return sum(len(pile) for pile in player.player_pile.values())
    
    def spit_pile_length(self,player):
        for pile in player.spit_pile.values():
            return len(pile)

    def deal_cards(self, player):
        while len(player.player_pile["pile1"]) < 1:
            player.player_pile["pile1"].append(self.cards.pop())

        while len(player.player_pile["pile2"]) < 2:
            player.player_pile["pile2"].append(self.cards.pop())

        while len(player.player_pile["pile3"]) < 3:
            player.player_pile["pile3"].append(self.cards.pop())

        while len(player.player_pile["pile4"]) < 4:
            player.player_pile["pile4"].append(self.cards.pop())

        while len(player.player_pile["pile5"]) < 5:
            player.player_pile["pile5"].append(self.cards.pop())
           
        while len(player.spit_pile["pile"]) < 11:
            player.spit_pile["pile"].append(self.cards.pop())
            
class Player:
    def __init__(self, name):
        self.name = name
        self.player_pile = {
                "pile1": [],
                "pile2": [],
                "pile3": [],
                "pile4": [],
                "pile5": []
                }
        self.spit_pile = {"pile": []}
        
    def show_player_piles(player):
        for (name, pile) in player.player_pile.items():
            print(f"{name}: {pile}") #Prints cards from 5 piles
            print("\n")
        print(f"Spit Pile: {player.spit_pile['pile']}") #Prints from spit pile
        
    def show_player_unicode_piles(self):
        for (name, pile) in self.player_pile.items():
            unicode_cards = [str(card) for card in pile]  #Uses the __str__ 
            print(f"{name}: {unicode_cards}") #Prints cards from 5 piles
            print("\n")
        unicode_spit_pile= [str(card) for card in self.spit_pile["pile"]]
        print(f"Spit Pile: {unicode_spit_pile}")  #Prints from spit pile


deck = Deck() #Creates deck
deck.shuffle() #Shuffles deck
player = Player("Alice") #Create instance of player object 
deck.deal_cards(player) #Gives cards to the player 

#Shows total cards in all 5 piles
print(f"Total cards in 5 piles: {deck.deck_length(player)}") 
#Shows total cards in the spit pile     
print(f"Total cards in spit pile: {deck.spit_pile_length(player)}")  
print("\n")
#Shows all the cards that the player has 
print(f"Here are {player.name}'s Piles:\n")
player.show_player_unicode_piles()   