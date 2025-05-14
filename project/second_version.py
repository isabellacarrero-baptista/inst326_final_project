import random
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from argparse import ArgumentParser
import sys

with open('cards.json', 'r') as file:
    cards_data = json.load(file)

class Card:
    """Represents a playing card.

    Author: Josue Miguel

    Attributes:
        rank (str): The rank of the card (e.g., "Ace", "2", "King").
        suit (str): The suit of the card (e.g., "Spades", "Hearts", ect)
    """
    rank_values = cards_data["ranks"]  

    def __init__(self, rank, suit):
        """Initializes a Card object with a rank and a suit.

        Args:
            rank (str): The rank of the card.
            suit (str): The suit of the card.
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """Returns a string representation of the card.

        Returns:
            str: A string in the format 'rank of suit' (e.g., 'Ace of Spades').
        """
        return f"{self.rank} of {self.suit}"

    def value(self):
        """Returns the numerical value of the card based on its rank.

        Returns:
            int: The numerical value of the card (e.g., 'Ace' it would return 1)
        """
        return Card.rank_values[self.rank]

    def __str__(self):
        """Returns a string representation of the card with suit symbols.

        Returns:
            str: A string in the format with suit symbols (e.g., 'Ace of ♠')
        """
        suit_symbols = {
            "Spades": "\u2660",     # ♠
            "Hearts": "\u2665",     # ♥
            "Diamonds": "\u2666",   # ♦
            "Clubs": "\u2663"       # ♣
        }
        return f"{self.rank}{suit_symbols[self.suit]}"

class Deck:
    """Represents a deck of playing cards.

    Author: Josue Miguel

    Attributes:
        cards (list): A list of Card objects representing a full deck.
    """
    def __init__(self):
        """Initializes the deck and creates it with 52 cards"""
        self.cards = []
        for rank in cards_data["ranks"]:
            for suit in cards_data["suits"]:
                self.cards.append(Card(rank, suit))

    def show(self):
        """Displays all the cards in the deck."""
        for card in self.cards:
            print(card)

    def shuffle(self):
        """Shuffles the cards in the deck."""
        random.shuffle(self.cards)
        
    def deck_length(self, player):
        """Calculates the total number of cards held by the player.

        Args:
            player (Player): The player whose piles are to be counted.

        Returns:
            int: The total number of cards in the player's piles.
        """
        return sum(len(pile) for pile in player.player_pile.values())
    
    def spit_pile_length(self, player):
        """Calculates the number of cards in the player's spit pile.

        Args:
            player (Player): The player whose spit pile is to be counted.

        Returns:
            int: The number of cards in the player's spit pile.
        """
        for pile in player.spit_pile.values():
            return len(pile)

    def deal_cards(self, player):
        """Deals cards to the player, distributing them across five piles.
        Each pile will contain the cards associated with their number
        For example: 1 card for pile 1
                     2 cards for pile 2
                     3 cards for pile 3
                     4 cards for pile 4
                     5 cards for pile 5
        Args:
            player (Player): The player to whom the cards are being dealt.
        """
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
        '''Returns a list of all card values in the player's piles.

        Returns:
            list: A list of all card values in the player's piles.
        '''
        all_cards = []
        for pile in self.player_pile.values():
            all_cards.extend(pile)
        all_cards.extend(self.spit_pile["pile"])
        return all_cards

    def show_player_piles(self):
        for (name, pile) in self.player_pile.items():
            print(f"{name}: {pile}")  # Prints cards from 5 piles
            print("\n")
        print(f"Spit Pile: {self.spit_pile['pile']}")  # Prints from spit pile

    def show_player_unicode_piles(self):
        for (name, pile) in self.player_pile.items():
            unicode_cards = [str(card) for card in pile]  # Uses the __str__ 
            print(f"{name}: {unicode_cards}")  # Prints cards from 5 piles
        unicode_spit_pile = [str(card) for card in self.spit_pile["pile"]]
        print(f"Spit Pile: {unicode_spit_pile}")  # Prints from spit pile

    def face_up_cards(self):
        """Gets the face-up card from the player pile and spit pile.

        Returns:
            dict: A dictionary mapping pile names to the top card in each pile.  
        """
        face_up = {}
        for pile_name, pile in self.player_pile.items():
            if pile:  # non-empty pile
                face_up[pile_name] = pile[-1]  # top card is last in list
        if self.spit_pile["pile"]:
            face_up["spit"] = self.spit_pile["pile"][-1]
        return face_up

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
        )
        
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
        face_up = self.face_up_cards()

        for pile_name, card in face_up.items():
            for index, center_pile in enumerate(center_spit_piles):
                if not center_pile:
                    continue
                center_card = center_pile[-1]
                if self.card_playable(card, center_card):
                    if pile_name not in legal_plays_dict:
                        legal_plays_dict[pile_name] = []
                    legal_plays_dict[pile_name].append(index + 1)
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
                    center_piles[index].append(self.player_pile[pile].pop())
                    self.flip_next_card(pile)
                    return True
        return False 

    def flip_next_card(self):
        next_cards = []
        for pile_name, pile in self.player_pile.items():
            if pile:
                next_cards.append(pile[-1])  
        print(f"Next Cards: {next_cards}")
    
    def win_condition(self):
        """Checks if the player has won. A player wins if they have no more 
        cards left.

        Args:
            self (player): the player whose piles are being checked if they're 
            empty or not.

        Returns:
            bool: True if all piles are empty (AKA the player won)
        """
        for cards in self.player_pile.values():
            if cards:
                return False 
        if self.spit_pile["pile"]:
            return False
        
        print("You are the winner!")
        return True

def move_empty_pile(player):
    """Moves a pile over to an empty pile.

    Args:
        player (Player): the player moving the pile.
    """
    for pile_name, pile in player.player_pile.items():
        if not pile:
            next_pile = f"pile{len(player.player_pile) + 1}"
            print(f"Moving {pile_name} over to {next_pile}")
            player.player_pile[next_pile] = pile

def game_statistics(player1, player2):
    """Prints the statistics of the game play.

    Args:
        player1 (Player): the first player in the game.
        player2 (Player): the second player in the game.
    """
    print(f"{player1.name}'s Remaining Cards: {player1.deck_length(player1)} cards.")
    print(f"{player2.name}'s Remaining Cards: {player2.deck_length(player2)} cards.")

def card_action(action):
    """Returns a simple action for the cards.

    Args:
        action (str): the type of action requested by the user.
    """
    action_list = {
        "help": "\n  Help: Move your card", 
        "stats": "\n  Stats: Show player stats",
        "play": "\n  Play a card", 
        "flip": "\n  Flip the next card in pile",
        "exit": "\n  Exit: End the game"
    }
    
    return action_list.get(action.lower(), "Invalid action!")

def main():
    """Main function to drive the game logic."""

    # Command-line argument parsing.
    parser = ArgumentParser()
    parser.add_argument("--deck", action="store_true", help="Show full deck")
    parser.add_argument("--name", type=str, required=True, help="Player name")
    parser.add_argument("--opponent", type=str, required=True, help="Opponent name")
    parser.add_argument("--action", type=str, help="Action to be executed")
    
    args = parser.parse_args()

    # Initialize the game and the deck
    deck = Deck()

    player1 = Player(args.name)
    player2 = Player(args.opponent)

    # Deal cards
    deck.deal_cards(player1)
    deck.deal_cards(player2)

    # Show full deck if requested
    if args.deck:
        deck.show()

    # Game loop
    print(f"{player1.name} vs {player2.name}")
    game_active = True
    while game_active:
        action = input(f"Choose an action ({player1.name}): ")
        if action.lower() == "exit":
            print("Exiting the game.")
            break
        elif action.lower() == "help":
            print(card_action("help"))
        elif action.lower() == "stats":
            game_statistics(player1, player2)
        elif action.lower() == "play":
            player1.card_to_center([player2.spit_pile["pile"]])
        elif action.lower() == "flip":
            player1.flip_next_card("")
        else:
            print("Invalid action!")
