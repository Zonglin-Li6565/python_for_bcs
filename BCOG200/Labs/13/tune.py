from bayes_opt import BayesianOptimization
from src import data_loader as dl
from src import logistic_regression as lr

INPUT_FILE_NAME = 'data/data3.csv'
OUTPUT_FILE_NAME = 'output.csv'
RANDOM_DATA = False
SVD_DIM = 0
VERBOSE = False
RANDOM_SEED = None


def main():
    normalization_map = [None, 'scale', 'z-score']

    def train(epoch, norm, lrate):
        my_data = dl.Dataset(INPUT_FILE_NAME, RANDOM_DATA, 0.75,
                             normalization_map[int(norm)], SVD_DIM, VERBOSE,
                             RANDOM_SEED)
        my_logreg = lr.LogisticRegression(my_data, lrate, int(epoch), VERBOSE,
                                          RANDOM_SEED, OUTPUT_FILE_NAME)
        my_logreg.train()
        return my_logreg.test()

    pbounds = {'epoch': (100, 1000), 'norm': (0, 2.9), 'lrate': (1e-2, 1e-1)}

    optimizer = BayesianOptimization(
        f=train,
        pbounds=pbounds,
        random_state=4352,
    )

    optimizer.maximize(init_points=4, n_iter=10)


main()
