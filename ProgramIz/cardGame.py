import random
import itertools


def build_deck():
    c_faces = ["Spades", "Hearts", "Diamonds", "Clubs"]
    c_nums = list(range(2,11))
    odd_nums = ["Ace", "Jack", "Queen", "King"]
    c_nums.extend(odd_nums)

    deck = list(itertools.product(c_faces, c_nums))
    if len(deck) != 52:
        return f"Deck count off: {len(deck)}. Expect 52."
    else:
        random.shuffle(deck)
        return deck

def card_draw(deck, num=5):
    """Deck is 52 tuples from list.
    Draw five tuples (default) and return"""
    return random.sample(deck, num)

shuffled = build_deck()

my_cards = card_draw(shuffled, 5)

print(f"My hand looks like...")
for c in my_cards:
    print(f"{c[1]} of {c[0]}")
