import random

def deal_player_cards(player):
    all_cards = player.values()
    random.shuffle(all_cards)
    for card in all_cards:
        player["pile1"].append(all_cards.pop())
        while len(player["pile2"]) < 2:
            player["pile2"].append(all_cards.pop())
        while len(player["pile3"]) < 3:
            player["pile3"].append(all_cards.pop())
        while len(player["pile4"]) < 4:
            player["pile4"].append(all_cards.pop())
        while len(player["pile5"]) < 5:
            player["pile5"].append(all_cards.pop())
        while card in all_cards:
            player["spit"].append(all_cards)

def deal_cards_under_15(player):
    all_cards = player.values()
    random.shuffle(all_cards)
    while all_cards:
        player["pile1"].append(all_cards.pop())
        player["pile2"].append(all_cards.pop())
        player["pile3"].append(all_cards.pop())
        player["pile4"].append(all_cards.pop())
        player["pile5"].append(all_cards.pop())
               
# The following is not my code- this is Josue's- but I am using it as it will be
# incorporated into the final code for this portion of the game.        
def win_condition(player):
#Iterates over every card in the player.values(), if the pile has a cards it 
#returns False, by default it returns True
    for cards in player.values():
        if cards:
            print("You are not the winner!")
            return True 
    print("You are the winner!")
    return False

# The following two functions are placeholder functions and will be properly
# incorporated into the final code. They are here to represent the
# functionality that will be implemented in the final code.

def playable_cards():
    spit_piles = ('Hearts', 3)
    faceup_cards = ('Diamonds', 2)
    top_spitcard = ('Clubs', 1)
    return True
    
def move_empty_pile(player):
    if player["pile1"] == []:
        print("You can move a card from pile 2 to pile 1.")
    if player["pile2"] == []:
        print("You can move a card from pile 3 to pile 2.")
    if player["pile3"] == []:
        print("You can move a card from pile 4 to pile 3.") 
    if player["pile4"] == []:
        print("You can move a card from pile 5 to pile 4.")           
    return True
    
def change_gamestate(player1, player2):
    # PLayer1 is the player who has reached <= 15 cards.
    
    # Setup
    
    deal_cards_under_15(player1)
    deal_player_cards(player2)
    
    spit_pile = []
    spit_pile[player2["spit"].pop()]
    # The following code would be implemented in the main function, but is 
    # represented here so that the value can be translated.
    player1_total = sum(len(pile) for pile in player1.values())  
    while player1_total <= 15:
        
        # Turn order
        
        turn = 0  
        if turn % 2 == 0:
            player_turn = player1
            print(f"{player1}'s turn!")
        else:
            player_turn = player2
            print(f"{player2}'s turn!")
        
        # Gampeplay loop
            
        if player_turn == player1:
            # The following code is is a placeholder for the function to 
            # to represent the main game loop that would be involved here.
            action = playable_cards()
            if action == None:
                print("You could not play a card! Moving to the next player.")
            # The following code is a placeholder for the function as well.
            # Same thing- it represents the main game loop that would occur here.
            move_empty_pile(player1)
        else:
            action = playable_cards()
            if action == None:
                print("You could not play a card! Moving to the next player.")
            move_empty_pile(player2)
        turn += 1
        if player1.values() == 0:
            print("You have no cards left! Reverse slapping pile.")
            
            # Assuming player becomes a class, they would have an attribute for 
            # their total cards.  This would be where it would be called, 
            # but for now, a placeholder will be used.
            all_cards = player1.values()
            
            player2[all_cards].append(spit_pile)
            return win_condition(player1)
        elif player1.values() > 0 and player1.values() <= 15:
            pass
        else:
            print("You have more than 15 cards! Returning to the normal" \
                " gamestate.")
            break