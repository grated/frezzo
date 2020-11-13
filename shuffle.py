#!/usr/bin/python3

import random

deck = list(range(1, 19))

hand = random.sample(deck, k=3)

print(hand)
