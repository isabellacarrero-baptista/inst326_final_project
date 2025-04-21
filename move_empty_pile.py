""" Hong: When one of the five piles is empty, 
move a card from the pile into the empty pile 
and turn over the next card in the pile that the card was taken from. 

The algorithm will need:

-The state of all five piles 
-Player input if they want to move a card
-Error if player cannot move card to empty pile

Results:

-Updated values of the face up cards
-Updated values of the pile
-Change in values in the five piles 
"""

def move_empty_pile(player):
    response = input("Do you want to move a card to a empty pile? [y/n] ")
    response = response.lower()
    check_empty = []
    is_empty = False
    if response == "yes" or response == "y":
        for pile in player: #check if piles are empty
            empty = []
            if player[pile] == empty:
                check_empty.append(True)
                is_empty = True
            else:
                check_empty.append(False)
        
        if not is_empty == True: #there is not an empty pile
            raise TypeError("There must be a empty pile.")
        else:
            try:
                pile_choice = int(input(f"Which card do you want to move? "
                                    "Name the pile from 1 to 5."))
                if pile_choice < 1 and pile_choice > 5:
                    raise IndexError
                elif check_empty[pile_choice-1] == True: #pile is empty
                    raise ValueError    
            except IndexError:
                print("Please enter a corresponding pile between 1 to 5.")
                pile_choice = input()
            except ValueError:
                print("Please enter a valid pile.")
            else: 
                added_to_empty = False
                pile_choice = pile_choice - 1
                keys_list = list(player.keys())
                popping_pile = keys_list[pile_choice]
                popped_card = player[popping_pile].pop()
                
                for pile in check_empty:
                    #update popped card to first empty pile
                    if added_to_empty == False and pile == True:
                        player[popping_pile].append(popped_card)
                        added_to_empty = True
                                      
    else: #response == no
        pass
                