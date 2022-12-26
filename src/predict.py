import pandas as pd
import pickle
import os
import sys
import warnings

warnings.filterwarnings("always")  

from utils.data_split import data_split
from utils.normalization import min_max_normalization
from utils.decision_path import get_decision_path

def main(args):
    ### Load dataset
    if len(args) > 1:
        predict_path = os.path.join("dataset", args[1])
    else:
        predict_path = os.path.join("dataset", "predict_example.csv")

    df = pd.read_csv(predict_path)

    ### Normalization
    _, X_test = min_max_normalization(test_set=df, mode="predict")

    print("X_test", X_test.values)
    ### Load Model
    filename = os.path.join("model", "finalized_model.sav")
    file = open(filename, "rb")
    model = pickle.load(file)
    file.close()

    ### Prediction
    model_result = model.predict(X_test.values)

    get_decision_path(model, X_test)

    print("result", model_result)

if __name__ == "__main__":
    main(sys.argv)









