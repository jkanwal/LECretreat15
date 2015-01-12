#!/usr/bin/env python

# IMPORTS
from sys import argv
from scipy import random, spatial, stats


# MantelTest()
#   Takes two lists of pairwise distances and performs a Mantel test. Returns
#   the veridical correlation (r), the mean (m) and standard deviation (sd)
#   of the Monte Carlo sample correlations, and a Z-score (z) quantifying the
#   significance of the veridical correlation.

def MantelTest(distances1, distances2, randomizations):
    r = stats.pearsonr(distances1, distances2)[0]
    m, sd = MonteCarlo(distances1, distances2, randomizations)
    z = (r-m)/sd
    return r, m, sd, z


############ ReadFile() ############
#   Takes a filename as an argument. Opens the file and separates out the data
#   into two lists (strings and meanings). Returns those two lists.








############ END OF ReadFile() ############


############ PairwiseDistances() ############
#   Takes a list of strings. For each pair of strings, calculate the Levenshtein
#   edit distance and store it to a new list. Return this new list of pairwise
#   distances.








############ END OF PairwiseDistances() ############


############ MonteCarlo() ############
#   Takes two lists and a number of randomizations. Runs a loop for the number
#   randomizations. On each loop iteration, shuffle one of the lists using the
#   ShuffleDistances() function below, then correlate the two lists. Put all the
#   correlation values into another list. Finally, return the mean and standard
#   deviation of all these correlation values.








############ END OF MonteCarlo() ############


# LevenshteinDistance()
#   Takes two stirngs and returns the normalized Levenshtein distance

def LevenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1], distances[index1+1], newDistances[-1])))
        distances = newDistances
    return float(distances[-1])/max(len(s1), len(s2))


# ShuffleDistances()
#   Takes a list of pairwise distances, converts it to a distance matrix,
#   shuffles the matrix, and returns the upper triangle as a vector.

def ShuffleDistances(pairwise_distances):
    matrix = spatial.distance.squareform(pairwise_distances, 'tomatrix')
    shuffled_vector = []
    n = len(matrix)
    shuffle_order = range(0, n)
    random.shuffle(shuffle_order)
    c = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            shuffled_vector.append(matrix[shuffle_order[i]][shuffle_order[j]])
            c += 1
    return shuffled_vector


if __name__ == '__main__':
    strings, meanings = ReadFile(argv[1])
    pairwise_dist_strings = PairwiseDistances(strings)
    pairwise_dist_meanings = PairwiseDistances(meanings)
    r, m, sd, z = MantelTest(pairwise_dist_strings, pairwise_dist_meanings, 10000)
    print r, m, sd, z
