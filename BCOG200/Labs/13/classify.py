from src import data_loader as dl
from src import logistic_regression as lr
import numpy as np
from src import k_nearest_neighbors as knn
import matplotlib.pyplot as plt

RANDOM_SEED = None

# Dataset Parameters
TRAINING_PROPORTION = .1
NORMALIZE_METHOD = None   # options are 'scale', 'z-score'
SVD_DIM = 0

# KNN Parameters
SIMILARITY_METRIC = 'cosine'   # options are 'cosine', 'distance'
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
#RANDOM_DATA = (4, 5, 20)
# if you want to use random data, specify a tuple with 3 numbers:
# 0 num_categories
# 1 num_words per category
# 2 num randomly generated features

def main():
    # load the data.
    test_accuracies = []
    test_accuracy = []
    train_accuracy = []
    test_sdv = []
    train_sdv = []
    for split in [0.1, 0.3, 0.5, 0.7]:
        total_test_acc = []
        total_train_acc = []
        for _ in range(10):
            my_data = dl.Dataset(INPUT_FILE_NAME, RANDOM_DATA, split, NORMALIZE_METHOD, SVD_DIM, VERBOSE, RANDOM_SEED)

            # compute correlations between features and categories
            #my_data.compute_feature_correlations()

            # plot word scatterplot. by default, performs SVD and plots first 2 SVs. If you want to plot
            # if instead you want to plot specific features, use their numbers as arguments after WORD_LABELS
            #my_data.plot_feature_scatter(WORD_LABELS)  # include 2 features after WORD

            # plot scatterplot of words and their category assignments.
            # The first number is the feature number, the second number is the category number
            #my_data.plot_feature_category_scatter(WORD_LABELS, 1, 0)

            # hierarchical clustering of words in terms of their features
            #my_data.plot_hierarchical_cluster(similarity=True)

            # k-nearest neighbor model
            # my_knn = knn.Knn(my_data, MIN_MAX_KNN, SIMILARITY_METRIC, VERBOSE, RANDOM_SEED, OUTPUT_FILE_NAME)
            # my_knn.train()
            # my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)

            # logistic regression model
            my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE, RANDOM_SEED, OUTPUT_FILE_NAME)
            total_train_acc.append(my_logreg.train())
            total_test_acc.append(my_logreg.test())
        train_accuracy.append(sum(total_train_acc) / 10)
        test_accuracy.append(sum(total_test_acc) / 10)
        train_sdv.append(np.std(total_train_acc))
        test_sdv.append(np.std(total_test_acc))
        test_accuracies.append(total_test_acc)

    # a plot of the model's prediction scores versus reality
    # my_logreg.plot_ypredict_yactual_scatter(WORD_LABELS, 0)

    # a heatmap of the weights learned by the model
    # my_logreg.plot_weight_heat_map()

    # plt.show()

    print(test_accuracy)
    print(train_accuracy)
    print(train_sdv)
    print(test_sdv)
    print(test_accuracies)


main()

