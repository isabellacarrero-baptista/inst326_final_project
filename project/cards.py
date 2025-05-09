import json

suits = [
    'Hearts', 
    'Diamonds',
    'Clubs',
    'Spades'
    ]

    
ranks = {
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

card_data = {
    "suits": suits,
    "ranks": ranks
}

with open ('cards.json', 'w') as file:
    json.dump(card_data, file, indent=4)
    
with open ('cards.json', 'r') as file:
    cards = json.load(file)
    
for line in cards.items():
    print(line)