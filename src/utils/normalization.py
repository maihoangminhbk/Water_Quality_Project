import numpy as np

def min_max_normalization(train_set=[], test_set=[], mode="train"):
    if mode == "train":
        x_train_max = np.max(train_set)
        x_train_min = np.min(train_set)

    if mode == "predict":
        x_train_max = np.array(61227.19600771213)
        x_train_min = np.array(0)

    train_set = (train_set - x_train_min)/(x_train_max-x_train_min)
    test_set = (test_set - x_train_min)/(x_train_max-x_train_min)

    return train_set, test_set