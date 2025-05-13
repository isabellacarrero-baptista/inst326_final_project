#make basic visual title screen
#by Hong
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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
plt.show()