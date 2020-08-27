import numpy as np
import matplotlib.pyplot as plt

def getHackerList(m):
    hackersList = []
    for index in range(m):
        string = ""
        for char in range(4):
            string += chr(96 + np.random.randint(1, 27))

        hackersList.append(string)

    print(hackersList)
    return hackersList


# Testing
numberOfTests = 1000
k = 7
m = 1
myPW = "abcd"

# Hacking test w/ a list of "m" random PWs
mhackedCount = 0
for i in range(numberOfTests):
    if myPW in getHackerList(m):
        mhackedCount += 1

mHackedProb = mhackedCount / numberOfTests
print("Probability of my PW being amongst ", m, " hacked PWs:", mHackedProb, sep='')

# Hacking test w/ a list of "m * k" random PWs
mkHackedCount = 0
for i in range(numberOfTests):
    if myPW in getHackerList(m*k):
        mkHackedCount += 1

mkHackedProb = mkHackedCount / numberOfTests
print("Probability of my PW being amongst ", m * k, " hacked PWs:", mHackedProb, sep='')


