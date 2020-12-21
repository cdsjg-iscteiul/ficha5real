import itertools
import math
import numpy as num

# Euclidean distante
# d = Raizquadrada( (a-b)^2)

k = 11

combinations_10_all = list(map(list, itertools.product([0, 1], repeat=10)))


def return_1st(val):
    return val[0]


def make_sets():
    training_set = []
    test_set = []
    num.random.shuffle(combinations_10_all)
    for x in range(len(combinations_10_all)):
        if x <= 307:
            test_set.append(combinations_10_all[x])
        else:
            training_set.append(combinations_10_all[x])

    return [training_set, test_set]


def calculate_distante(bits1, bits2):
    result = 0
    for x in range(len(bits1)):
        result += (bits1[x] - bits2[x]) ** 2

    return num.sqrt(result)


def print_best(values):
    for x in range(k):
        print("VALOR:  " + str(values[x][0]) + "  COMBINAÇÃO TRAINING:  " + str(values[x][1]) + "  TEST:  " +
              str(values[x][2]))


def runner():
    full_sets = make_sets()
    training_set = full_sets[0]
    test_set = full_sets[1]
    values = []
    last_values = []
    for g in range(30):
        for x in range(len(test_set)):
            distance = calculate_distante(training_set[x], test_set[x])
            values.append([distance, training_set[x], test_set[x]])

    values.sort(key=return_1st, reverse=True)

    for tt in range(k):
        last_values.append(values[tt])

    print_best(values)


def splitting_lists():
    set1 = []
    set2 = []
    all_set = combinations_10_all
    for x in combinations_10_all:
        if x[1] == 0:
            set1.append(x)
        else:
            set2.append(x)

    entropy_1 = entropy(set1)
    entropy_2 = entropy(set2)
    entropy_all = entropy(all_set)


def gain(d, a):
    total = 0
    for x in a:
        total += sum(x) / sum(d) * entropy(x)

    ganho = entropy(d) - total
    return ganho


def entropy(set1):
    num_negative = 0
    num_positve = 0

    for x in set1:
        for tt in x:
            if tt < 0:
                num_negative += 1

            else:
                num_positve += 1

    percentagem_negative = num_negative / 100
    percentagem_positive = num_positve / 100
    value = - percentagem_positive * math.log(percentagem_positive, 2) - percentagem_negative * math.log(
        percentagem_negative, 2)

    return value


runner()
