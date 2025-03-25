# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))  # Fixed missing parenthesis

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):  # Fixed missing colon
    print(deck[i][0], "of", deck[i][1])  # Fixed missing parenthesis
