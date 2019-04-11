from src import data_loader as dl
from src import logistic_regression as lr
from src import k_nearest_neighbors as knn
import matplotlib.pyplot as plt

# Dataset Parameters
TRAINING_PROPORTION = .75
NORMALIZE = True
SVD_DIM = 0

# KNN Parameters
DISTANCE_METRIC = 'cosine'
MIN_MAX_KNN = (1, 5)

# Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000

# print amount parameters
VERBOSE = True

# plot option
WORD_LABELS = True

# data file
FILE_NAME = 'data/data2.csv'

# to use the data in the file, set RANDOM_DATA to False:
RANDOM_DATA = (4, 5, 20)
# if you want to use random data, specify a tuple with 3 numbers:
# 0 num_categories
# 1 num_words per category
# 2 num randomly generated features

def main():
    my_data = dl.Dataset(FILE_NAME, RANDOM_DATA, TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)
    my_data.compute_feature_correlations()
    # my_data.plot_feature_scatter(WORD_LABELS)
    # my_data.plot_feature_category_scatter(WORD_LABELS, 1, 0)

    my_knn = knn.Knn(my_data, MIN_MAX_KNN, DISTANCE_METRIC, VERBOSE)
    my_knn.train()
    my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)

    # my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE)
    # my_logreg.train()
    # my_logreg.test()
    # my_logreg.plot_ypredict_yactual_scatter(WORD_LABELS, 0)
    # my_logreg.plot_weight_heat_map()

    plt.show()


main()

