ranks = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King',
    'Ace'
    ]

#sets each rank to a numerical value so cards can be placed in increasing or 
# decreasing sequence
rank_value = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 1
}


def playable_cards(spit_piles, faceup_cards, top_spitcard):
    
    #dictionary for each legal play the player can make
    legal_plays_dict = {}
    
    #outlines in what order cards can be placed
    #cards have to be one number above or below each other
    #Ace can equal both 1 and 13
    def legal_plays(card_val, spit_val):
        return (
            abs(card_val - spit_val) == 1 or
            (card_val == 1 and spit_val == 13) or 
            (card_val == 13 and spit_val == 1)
        )
    
    #a list of the top cards in the spit pile in numerical values 
    spit_vals = [rank_value[card[0]] for card in spit_piles]
    
    #checks top face up cards in the 5 spit piles
    for index, card in enumerate(faceup_cards): 
        if card == None: 
            continue
        card_val = rank_value[card[0]]
        for spit_index, spit_val in enumerate(spit_vals):
            if legal_plays(card_val, spit_val):
                key = f"pile {index+1}"
                if key not in legal_plays_dict:
                    legal_plays_dict[key] = []
                legal_plays_dict[key].append(spit_index + 1)
                    
    #check top face down card on the player's spit stack they draw from
    if top_spitcard:
        spit_card_val = rank_value[top_spitcard[0]]
        for spit_index, spit_val in enumerate(spit_vals):
            if legal_plays(spit_card_val, spit_val):
                key = "spit"
                if key not in legal_plays_dict:
                    legal_plays_dict[key] = []
                legal_plays_dict[key].append(spit_index + 1)
                
    #raises an error telling the player they can't place a card there
    if not legal_plays_dict:
        raise Exception("That is an invalid play!")
                    
    return legal_plays_dict
        
                                        