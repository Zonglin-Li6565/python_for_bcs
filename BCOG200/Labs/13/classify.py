from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
from src import data_loader as dl
from src import logistic_regression as lr

RANDOM_SEED = None

# Dataset Parameters
SVD_DIM = 0

# KNN Parameters
SIMILARITY_METRIC = 'cosine'  # options are 'cosine', 'distance'
MIN_MAX_KNN = (1, 3)

# Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000

# print amount parameters
VERBOSE = False

# plot option
WORD_LABELS = True

# data file
INPUT_FILE_NAME = 'data/data3.csv'
OUTPUT_FILE_NAME = 'output.csv'

# to use the data in the file, set RANDOM_DATA to False:
RANDOM_DATA = False
# RANDOM_DATA = (4, 5, 20)
# if you want to use random data, specify a tuple with 3 numbers:
# 0 num_categories
# 1 num_words per category
# 2 num randomly generated features

normalization_options = [None, 'z-score']
tp_options = [0.10, 0.20, 0.50, 0.95]


def worker(params):
    print('Running', params)
    normalization_idx, tp_idx, id = params
    my_data = dl.Dataset(INPUT_FILE_NAME, RANDOM_DATA, tp_options[tp_idx],
                         normalization_options[normalization_idx], SVD_DIM,
                         VERBOSE, RANDOM_SEED)
    my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS,
                                      VERBOSE, RANDOM_SEED, OUTPUT_FILE_NAME)
    my_logreg.train()
    performance = my_logreg.test()
    return normalization_idx, tp_idx, id, performance


def main():
    # load the data.
    run_options = []
    for i in range(len(normalization_options)):
        for j in range(len(tp_options)):
            for k in range(30):
                run_options.append((i, j, k))

    results = np.zeros((2, 4, 30))

    with Pool(8) as pool:
        for i, j, k, performance in pool.map(worker, run_options):
            results[i, j, k] = performance

    means = results.mean(2)
    stds = results.std(2)

    fig, ax = plt.subplots()
    x_range = np.arange(4)
    width = 0.35
    p0 = ax.bar(x_range, means[0], width, color='b', bottom=0, yerr=stds[0])
    p1 = ax.bar(x_range + width, means[1], width, color='r', bottom=0,
                yerr=stds[1])
    ax.set_title('Performance of logistic regression vs normalization and tp')
    ax.set_xticks(x_range + width / 2)
    ax.set_xticklabels(tp_options)

    ax.legend((p0[0], p1[0]), ('None', 'z-score'))
    ax.set_xlabel('TP')
    ax.set_ylabel('Performance')
    ax.autoscale_view()

    plt.show()


main()
