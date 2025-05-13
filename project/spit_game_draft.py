import random
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


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

    def values(self):
        all_cards = []
        for pile in self.player_pile.values():
            all_cards.extend(pile)
        all_cards.extend(self.spit_pile["pile"])
        return all_cards
        
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
        """Checks if the card can be played on the center spit pile. 
        Uses conditional expression technique. 

        Args:
            card (Card): The player's card that can be played.
            center_spitpile_card (Card): The top card on the center spit pile.

        Returns:
            bool: True if the card can be played, False if it can't.
        """
        return (
            abs(card.value() - center_spitpile_card.value()) == 1 or
            (card.value() == 1 and center_spitpile_card.value() == 13) or 
            (card.value() == 13 and center_spitpile_card.value() == 1)
        ) if center_spitpile_card else False 
        
            
    def legal_plays(self, center_spit_piles):
        """All the legal moves a player can make. Checks the player's cards 
        against the center spit piles.

        Args:
            center_spit_piles (list): A list of two lists for each center spit
            pile.

        Returns:
            dictionary: dictionary of legal plays.
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
        """Attempts to play one legal card to a center spit pile.
        Uses f-sting technique.

        Args:
            center_piles (list): A list of two lists for each center spit
            pile.

        Returns:
            bool: True if a card was played, False if it wasn't.
        """
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
        
    #win method
    def win_condition(player):
        for cards in player.values():
            if cards:
                print("You are not the winner!")
                return False 
            else:
                print("You are the winner!")
                return True
        
                        
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
            other_player = player2
            print('\n')
            print(f"{player1.name}'s turn!")
        else:
            player_turn = player2
            other_player = player1
            print('\n')
            print(f"{player2.name}'s turn!")
        
        
        player_turn.show_player_unicode_piles()
        print('\n')
        print(f"Middle spit pile 1: {spit_piles["pile1"]}")
        print(f"Middlepit pile 2: {spit_piles["pile2"]}")
        print('\n')
        try:
            action = input("Choose an action: 'play', 'slap', or 'skip': ")
            action = action.lower()
            if action == "play":
                legal_moves = player_turn.legal_plays(list(spit_piles.values()))
                print(f"Legal moves: {legal_moves}")
                pile_choice = input("Pick a pile to play from (1-2): ")
                card_choice = input("Pick a card to play (1-5): ")
                if player_turn.card_playable(card_choice, pile_choice):
                    spit_piles[pile_choice].append(player_turn.player_pile\
                                                   [card_choice].pop())
                    #Check that last one lowk
            elif action == "slap":
                if len(player_turn.values()) == 0:
                    print("Pick a pile to slap: ")
                    print(len(spit_piles["pile1"]))
                    print(len(spit_piles["pile2"]))
                    pile_choice = input("Choose a pile (1 or 2): ")
                    if pile_choice == "1":
                        deck.cards.extend(spit_piles["pile1"])
                        deck.deal_cards(player_turn)
                        deck.cards.extend(spit_piles["pile2"])
                        deck.deal_cards(other_player)
                    elif pile_choice == "2":
                        deck.cards.extend(spit_piles["pile2"])
                        deck.deal_cards(player_turn)
                        deck.cards.extend(spit_piles["pile1"])
                        deck.deal_cards(other_player)
                else:
                    print("You cannot slap now.")
                    continue
            elif action == "skip":
                print("Skipping turn.")
            else:
                raise ValueError
        except ValueError:
            print("Invalid action. Please type 'play', 'slap', or 'skip'.")
            continue
            
        #if len(player_turn.values()) <= 15:
           # change_gamestate(player_turn)
        #if len(other_player.values()) <= 15:
            #change_gamestate(other_player)
        # Revise change_gamestate
        turn += 1
    
def title_screen():

    #define figure and axis
    fig, ax = plt.subplots()
    ax.set_facecolor('green')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    #add card to plot
    card1 = Rectangle((1, 1), 2, 3, edgecolor='black', facecolor='white', linewidth=2)
    card2 = Rectangle((4, 1), 2, 3, edgecolor='black', facecolor='white', linewidth=2)
    card3 = Rectangle((7, 1), 2, 3, edgecolor='black', facecolor='white', linewidth=2)
    card4 = Rectangle((10, 1), 2, 3, edgecolor='black', facecolor='white', linewidth=2)
    card5 = Rectangle((13, 1), 2, 3, edgecolor='black', facecolor='white', linewidth=2)

    title = Rectangle((6, 6), 4, 1.65, edgecolor='black', facecolor='white', linewidth=2)
    team = Rectangle((2, 4.5), 4.5, 1.25, edgecolor='black', facecolor='black', linewidth=2)
    members = Rectangle((9.5, 4.5), 4.5, 1.25, edgecolor='black', facecolor='red', linewidth=2)

    ax.add_patch(card1)
    ax.add_patch(card2)
    ax.add_patch(card3)
    ax.add_patch(card4)
    ax.add_patch(card5)
    ax.add_patch(title)
    ax.add_patch(team)
    ax.add_patch(members)

    #texts of card num
    card1_rank = '4'
    card1_suit = '\u2663'
    card2_rank = '7'
    card2_suit = '\u2666'
    card3_rank = 'Ace'
    card3_suit = '\u2665'
    card4_rank = '9'
    card4_suit = '\u2660'
    card5_rank = '11'
    card5_suit = '\u2663'

    #show texts
    ax.text(2, 2.5, card1_rank + ' ' + card1_suit, horizontalalignment='center', verticalalignment='center')
    ax.text(5, 2.5, card2_rank + ' ' + card2_suit, horizontalalignment='center', verticalalignment='center')
    ax.text(8, 2.5, card3_rank + ' ' + card3_suit, horizontalalignment='center', verticalalignment='center')
    ax.text(11, 2.5, card4_rank + ' ' + card4_suit, horizontalalignment='center', verticalalignment='center')
    ax.text(14, 2.5, card5_rank + ' ' + card5_suit, horizontalalignment='center', verticalalignment='center')

    ax.text(8, 6.75, 'Split', fontsize = 25, color = 'red', horizontalalignment='center', verticalalignment='center')
    ax.text(3, 5.35, 'By', fontsize = 8, color = 'white', horizontalalignment='center', verticalalignment='center')
    ax.text(4.25, 5, 'Saucy Syntax Squad', fontsize = 8, color = 'white', horizontalalignment='center', verticalalignment='center')
    ax.text(11, 5.35, 'INST326', fontsize = 8, color = 'white', horizontalalignment='center', verticalalignment='center')
    ax.text(11.25, 5, 'Isabella, Josue,', fontsize = 8, color = 'white', horizontalalignment='center', verticalalignment='center')
    ax.text(12.35, 4.75, 'Ethan, Hong', fontsize = 8, color = 'white', horizontalalignment='center', verticalalignment='center')

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return plt.show()                    

    
    
if __name__ == "__main__":
    title_screen()
    main()






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

    
    
   
