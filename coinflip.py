#!/usr/bin/python3

import numpy as np

# probability of heads vs. tails
probability = .5
# num of flips required
n = 1

# initiate array
fullResults = np.arange(n)

def coinFlip(p):
    # perform the binomial distribution (returns 0 or 1)
    result = np.random.binomial(1,p)

    # return flip to be added to numpy array
    return result

# perform desired number of flips at required probability set above
for i in range(0,n):
    fullResults[i] = coinFlip(probability)
    i+=1

# print results
# print("probability is set to ", probability) # print the probability
print("Tails = 0, Heads = 1: ", fullResults)
# Add total amount of heads and tails
print("Heads: ", np.count_nonzero(fullResults == 1))
print("Tails: ", np.count_nonzero(fullResults == 0))
