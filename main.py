import itertools
import math
import numpy as num
import \
    matplotlib.pyplot as plt
# Euclidean distante
# d = Raizquadrada( (a-b)^2)

ks = [3, 7, 11]
splits = [0.3, 0.4, 0.5]

n_fig = 1

combinations_10_all = list(map(list, itertools.product([0, 1], repeat=10)))

def return_1st(val):
    return val[0]


def atib(bits):
    if sum(bits) >= 5:
        return "A"
    else:
        return "B"


def make_sets(split):
    training_set = []
    test_set = []
    num.random.shuffle(combinations_10_all)

    for i in range(len(combinations_10_all)):
        for h in range(len(combinations_10_all[i])):
            if combinations_10_all[i][h] == 0:
                combinations_10_all[i][h] = -1

    print(combinations_10_all)

    for x in range(len(combinations_10_all)):
        if x <= int(len(combinations_10_all) * split):
            test_set.append([combinations_10_all[x], 'clac'])
        else:
            training_set.append([combinations_10_all[x], atib(combinations_10_all[x])])

    return [training_set, test_set]


def calculate_distante(bits1, bits2):
    result = 0
    for x in range(len(bits1)):
        result += (bits1[x] - bits2[x]) ** 2

    return num.sqrt(result)


def runner():
    global n_fig
    values = [[], [], []]

    for i in range(30):
        for k in ks:
            sets = make_sets(ks.index(k))
            test = sets[1]
            train = sets[0]

            for x in range(len(test)):
                distances = []
                for j in train:
                    distance = calculate_distante(j[0], test[x][0])
                    distances.append([distance, j[0], j[1]])

                distances.sort()
                k_closest = distances[:k]

                votos_A = 0
                votos_B = 0
                for yy in k_closest:
                    if yy[1] == "A":
                        votos_A += 1
                    else:
                        votos_B += 1

                if votos_A > (k // 2):
                    test[x][1] = "A"
                else:
                    test[x][1] = "B"

            equal = 0
            for ii in test:
                og_class = atib(ii[0])
                new_class = ii[1]
                if og_class == new_class:
                    equal += 1
            percentage = equal / len(test) * 100
            values[ks.index(k)].append(round(percentage, 0))

    fig, ax1 = plt.subplots(1, 1)
    ax1.boxplot(values, labels=ks, vert=True)
    ax1.legend(['Figure ' + str(n_fig)], handlelength=0)
    n_fig += 1
    plt.show()


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
