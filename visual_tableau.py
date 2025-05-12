#make basic visual
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

ax.add_patch(card1)
ax.add_patch(card2)
ax.add_patch(card3)
ax.add_patch(card4)
ax.add_patch(card5)

#texts of card num
card1_rank = '5'
card1_suit = '\u2660'
card2_rank = '8'
card2_suit = '\u2665'
card3_rank = 'Queen'
card3_suit = '\u2666'
card4_rank = '9'
card4_suit = '\u2666'
card5_rank = 'Ace'
card5_suit = '\u2663'

#show texts
ax.text(2, 2.5, card1_rank + ' of ' + card1_suit, horizontalalignment='center', verticalalignment='center')
ax.text(5, 2.5, card2_rank + ' of ' + card2_suit, horizontalalignment='center', verticalalignment='center')
ax.text(8, 2.5, card3_rank + ' of ' + card3_suit, horizontalalignment='center', verticalalignment='center')
ax.text(11, 2.5, card4_rank + ' of ' + card4_suit, horizontalalignment='center', verticalalignment='center')
ax.text(14, 2.5, card5_rank + ' of ' + card5_suit, horizontalalignment='center', verticalalignment='center')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()