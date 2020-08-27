import numpy as np
import matplotlib.pyplot as plt


# p is a list of probabilities summation of
def nSidedDie(p):
    probSum = 0
    roll = np.random.rand()
    for index, val in enumerate(p):
        if probSum < roll <= probSum + val:
            outcome = index + 1
        probSum += val

    if probSum != 1:
        return 0

    return outcome


numberOfRolls = 10000
p = [0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10]
# Empty list of len(p) for counting frequency of roll outcomes
results = [0] * (len(p) + 1)
for i in range(numberOfRolls):
    results[nSidedDie(p)] += 1

# Plot
plt.close('all')
bins = range(1, len(p) + 1)
plt.stem(bins, results[1:])
plt.title("10,000 rolls of N-sided die")
plt.xlabel('Value of Die Face')
plt.ylabel('Times Value was Rolled')
plt.show()

