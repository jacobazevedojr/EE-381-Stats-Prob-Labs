import numpy as np
import random
import string
import matplotlib.pyplot as plt

def getHackerList(m):
    hackersList = []
    # Creates a list of "passwords" of 4 characters ranging from a-z
    for index in range(m):
        # Creates a string with each character randomized from a-z
        str1 = ''.join(random.choices(string.ascii_lowercase, k=4))

        hackersList.append(str1)

    return hackersList


# Testing
numberOfTests = 1000
k = 7
m = 80000
myPW = "abcd"

# Hacking test w/ a list of "m" random PWs
# Number of times "my password" was found while running "numberOfTests" tests on hackerLists w/ "m" words
mhackedCount = 0
for i in range(numberOfTests):
    if myPW in getHackerList(m):
        mhackedCount += 1

mHackedProb = mhackedCount / numberOfTests
# 16%
print("Probability of my PW being amongst a list of ", m, " hacked PWs:", "%.2f" % mHackedProb, sep='')
print()

# Hacking test w/ a list of "m * k" random PWs
# Number of times "my password" was found while running "numberOfTests" tests on hackerLists w/ "m*k" words
mkHackedCount = 0
for i in range(numberOfTests):
    print(i, end=' ')
    if i % 10 == 9:
        print()
    if myPW in getHackerList(m*k):
        mkHackedCount += 1

print()
mkHackedProb = mkHackedCount / numberOfTests
# 67%
print("Probability of my PW being amongst a list of ", m * k, " hacked PWs:", "%.2f" % mkHackedProb, sep='')

# Iterative test to discover how many words are needed in a hackerList to find "my password" half the time
# There are 456976 possible words in a 4 character password w/ all characters ranging from a-z
# This would mean that statistically, if a hackerList had this many random words, at least one would be "my PW"
# In order to have .5 probability, m must be somewhere between 456976 and 0
highM = 456976
currentM = 0
lowM = 0
foundProb = 1
while foundProb > .55 or foundProb < .45:
    numberFound = 0

    for i in range(numberOfTests):
        if i % 1 == 0:
            print(" . ", end='')
        if myPW in getHackerList(currentM):
            numberFound += 1

    print("yes")
    foundProb = numberFound / numberOfTests
    print

    # Binary search to find m that satisfies the equation .45 < foundProb < .55
    if foundProb < .6:
        lowM = currentM + 1
        currentM = (currentM + highM) // 2
    else:
        highM = currentM - 1
        currentM = (currentM + lowM) // 2

#399854
print("Number of words required to find my password 50% of the time:", currentM)
