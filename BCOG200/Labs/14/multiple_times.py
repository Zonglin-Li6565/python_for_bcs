import random
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
from src import datasets
from src import neural_network


def run_model(dataset, hidden_size, learning_rate, weight_stdev, num_epochs):
    # the network parameters
    num_input_units = dataset.x_size  # the number of input units in the
    # neural network, i.e. the # of features
    num_output_units = dataset.y_size  # the number of output units in the
    # network, i.e. the # of categories
    hidden_size = hidden_size  # the number of hidden units in the layer
    # between the inptus and the outputs
    learning_rate = learning_rate  # what fraction of the correct amount the
    # weights are changed on each trial
    weight_stdev = weight_stdev  # weights are initialized randomly to a
    # value with a mean of 0, and a stdev of this
    num_epochs = num_epochs  # how many epochs (passes through the full
    # dataset) the network takes

    # create the network
    net = neural_network.NeuralNetwork(num_input_units,
                                       hidden_size,
                                       num_output_units,
                                       learning_rate,
                                       weight_stdev)

    # test the random network's performance
    start_accuracy, start_error = net.test(dataset.training_x_list,
                                           dataset.training_y_list,
                                           dataset.training_label_list)

    # train the network
    train_accuracy, train_error_mean = net.train(dataset.training_x_list,
                                                 dataset.training_y_list,
                                                 num_epochs)

    # test the network
    test_accuracy, test_error_mean = net.test(dataset.test_x_list,
                                              dataset.test_y_list,
                                              dataset.test_label_list)

    # gather the information we want to return

    features = dataset.feature_list.copy()
    features.insert(0, 'X0')

    labels = (dataset.category_list, features)
    network_parameters = (
        num_input_units, num_output_units, hidden_size, net.h_x, net.y_h)
    weights = (
        np.vstack([net.h_bias, net.h_x.T]).T,
        np.vstack([net.y_bias, net.y_h.T]).T)
    training_parameters = (learning_rate, weight_stdev, num_epochs)
    performance = (
        train_accuracy, train_error_mean, test_accuracy, test_error_mean)

    return labels, network_parameters, weights, training_parameters, performance


def plot_performance(perf_mean, perf_std, loss_mean, loss_std, ax):
    ax.set_xlabel('Epochs')
    ax.set_ylabel('Accuracy', color='darkblue')
    epochs = range(perf_mean.shape[0])
    ax.plot(epochs, perf_mean, color='darkblue')
    ax.fill_between(epochs, perf_mean - perf_std, perf_mean + perf_std)

    ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

    # we already handled the x-label with ax1
    ax2.set_ylabel('SSE', color='orangered')
    ax2.plot(epochs, loss_mean, color='orangered')
    ax2.fill_between(epochs, loss_mean - loss_std, loss_mean + loss_std)


def worker(params):
    print('Running', params)
    (training_proportion, hidden_size, learning_rate, weight_stdev,
     num_epochs) = params
    animal_dataset = datasets.AnimalDataset('data/animals_4_128_15.csv',
                                            training_proportion)
    animal_model = run_model(animal_dataset, hidden_size, learning_rate,
                             weight_stdev, num_epochs)
    training_accuracy = animal_model[4][0]
    training_sse = animal_model[4][1]
    return training_accuracy, training_sse


NUM_CORES = 8


def run_multiple_models(model_config):
    accuracy = []
    loss = []
    with Pool(NUM_CORES) as pool:
        for acc, sse in pool.map(worker, model_config):
            accuracy.append(acc)
            loss.append(sse)
    return accuracy, loss


def main():
    np.set_printoptions(precision=3, suppress=True)
    random.seed(None)
    np.random.seed(None)

    model1_config = [(0.75, 1, 0.01, 0.5, 2000)] * 20

    model2_config = [(0.75, 4, 0.01, 0.5, 2000)] * 20

    model1_acc, model1_loss = run_multiple_models(model1_config)
    model2_acc, model2_loss = run_multiple_models(model2_config)

    model1_acc = np.array(model1_acc)
    model1_loss = np.array(model1_loss)

    model2_acc = np.array(model2_acc)
    model2_loss = np.array(model2_loss)

    fig, axis = plt.subplots(1, 2)
    ax1, ax2 = axis

    ax1.set_title('1 hidden unit')
    ax2.set_title('4 hidden units')
    plot_performance(model1_acc.mean(axis=0), model1_acc.std(axis=0),
                     model1_loss.mean(axis=0), model1_loss.std(axis=0), ax1)
    plot_performance(model2_acc.mean(axis=0), model2_acc.std(axis=0),
                     model2_loss.mean(axis=0), model2_loss.std(axis=0), ax2)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    plt.show()


if __name__ == '__main__':
    main()
