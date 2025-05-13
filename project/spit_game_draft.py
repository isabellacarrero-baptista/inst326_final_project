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
        
   
    #face_up_cards method Hong
    def face_up_cards(self):
        face_up_cards = []
        for piles in self.player_piles:
            face_up_cards.append(self.player_piles[piles].cards.pop(0))
        print(f"Face Up Cards: {face_up_cards}")
    
    #Isabella code for Player class:
    
    def card_playable(self, card, center_spitpile_card):
        """_summary_ 
        Uses conditional expression 

        Args:
            card (_type_): _description_
            center_spitpile_card (_type_): _description_

        Returns:
            _type_: _description_
        """
        return (
            abs(card.value() - center_spitpile_card.value()) == 1 or
            (card.value() == 1 and center_spitpile_card.value() == 13) or 
            (card.value() == 13 and center_spitpile_card.value() == 1)
        ) if center_spitpile_card else False 
        
            
    def legal_plays(self, center_spit_piles):
        """_summary_
        Uses fstring technique

        Args:
            center_spit_piles (_type_): _description_

        Returns:
            _type_: _description_
        """
        legal_plays_dict = {}
        
        #calls method for face-up cards        
        face_up = self.face_up_cards()

        for pile_name, card in face_up.items():
            for index, center_pile in enumerate(center_spit_piles):
                center_card = center_pile[-1] if center_pile else None 
                if self.card_playable(card, center_card):
                    if pile_name not in legal_plays_dict:
                        legal_plays_dict[pile_name] = []
                    legal_plays_dict[pile_name].append(index + 1)
                    
                    
        if self.spit_pile["pile"]:
            top_spit_card = self.spit_pile["pile"][-1]
            for index, center_pile in enumerate(center_spit_piles):
                center_card = center_pile[-1] if center_pile else None 
                if self.card_playable(top_spit_card, center_card):
                    if "spit" not in legal_plays_dict:
                        legal_plays_dict["spit"] = []
                    legal_plays_dict["spit"].append(index + 1) 
                    
        return legal_plays_dict
    
    def card_to_center(self, center_piles):
        face_up = self.face_up_cards()
      
        for pile, card in face_up.items():
            for index in range(len(center_piles)):
                if self.card_playable(card, center_piles[index][-1]):
                    print(f"{self.name} plays {card} from {pile} to center pile" 
                          f"{index + 1}")
                    center_piles[index].append(self.player_pile(pile).pop())
                    #calls flip_next_card method 
                    self.flip_next_card(pile)
                    return True
        return False 
    
    #flip_next_card method Hong
    def flip_next_card(self):
        next_cards = []
        for piles in self.player_piles:
            next_cards.append(self.player_piles[piles].cards.pop(0))
        print(f"Next Cards: {next_cards}")
        
                        
def main():
    deck = Deck()
    deck.shuffle()
    
    player1 = input("Enter a name for Player 1: ")
    player1 = Player(player1)
    
    player2 = input("Enter a name for Player 2: ")
    player2 = Player(player2)
    
    deck.deal_cards(player1)
    deck.deal_cards(player2)
    spit_piles = {
        "pile1": [],
        "pile2": []
    }
    spit_piles["pile1"].append(player1.spit_pile["pile"].pop())
    spit_piles["pile2"].append(player2.spit_pile["pile"].pop())
    
    turn = 0
    
    while True:
        if turn % 2 == 0:
            player_turn = player1
            print(f"{player1}'s turn!")
        else:
            player_turn = player2
            print(f"{player2}'s turn!")
        
        
        player_turn.show_player_unicode_piles()
        try:
            action = input("Choose an action: \
                'play' a card, 'slap', or 'skip': ")
            action = action.lower()
            if action == "play":
                player_turn.legal_plays()
                pile_choice = input("Pick a pile to play from: ")
                card_choice = input("Pick a card to play: ")
                if player_turn.card_playable(card_choice, pile_choice):
                    spit_piles[pile_choice].append(player_turn.player_pile\
                                                   [card_choice].pop())
                    #Check that last one lowk
            elif action == "slap":
                if sum(len(pile) for pile in player_turn.values()) == 0:
                    print("Pick a pile to slap: ")
                    print(len(spit_piles["pile1"]))
                    print(len(spit_piles["pile2"]))
                    pile_choice = input("Choose a pile (1 or 2): ")
                    if pile_choice == "1":
                        # make player's cards the slappe pile, other player's
                        # cards the otherpile
            elif action == "skip":
                print("Skipping turn.")
        except ValueError:
            print("Invalid input. Please try again.")
            continue
            
        player1_total = sum(len(pile) for pile in player1.values())
        player2_total = sum(len(pile) for pile in player2.values())
       # if player1_total <= 15:
           # change_gamestate(player1)
       # if player2_total <= 15:
           # change_gamestate(player2)
        # Revise change_gamestate
        turn += 1






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

    
    
   
