import pandas as pd
import pickle

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

import seaborn as sns
import matplotlib.pyplot as plt
from dtreeviz.trees import *
import graphviz

import os
import sys
import warnings
warnings.filterwarnings("always")  
import datetime

from utils.data_split import data_split
from utils.normalization import min_max_normalization

def main(args):
    ### Load dataset
    if "--f" in args:
        file_index = args.index("--f") + 1
        dataset_path = os.path.join("dataset", args[file_index])
    else:    
        dataset_path = os.path.join("dataset", "water_potability.csv")

    df = pd.read_csv(dataset_path)

    X =  df.drop("Potability",axis=1).values
    y =  df["Potability"].values

    ### Split data to train and test
    X_train, X_test, y_train, y_test = data_split(df, test_size=0.33)
    X_train, X_test = min_max_normalization(X_train, X_test, mode="train")

    ### Train Model
    model = DecisionTreeClassifier(criterion="entropy", max_depth=10, min_samples_leaf=50,
                       min_samples_split=5, random_state=42)

    model.fit(X_train, y_train)

    time_str = str(datetime.datetime.now())
    save_path = os.path.join("result", "train", time_str)
    os.mkdir(save_path)

    # Visualize
    if "--visualize" in args:
        fig = plt.figure(figsize=(25,20))
        viz = dtreeviz(model,
                X_train,
                y_train,
                target_name="water quality",
                feature_names=df.columns,
                title="Water data set classification",
                class_names=["0", "1"],
                scale=1.2)

        visualization_filename = os.path.join(save_path, "visualization_trained_tree.svg")
        viz.save(visualization_filename)
    
    plt.figure(figsize = (25,20))
    tree.plot_tree(model,
                feature_names =  df.columns.tolist()[:-1],
                class_names = ["0", "1"],
                filled = True,
                precision = 5)
    visualization_filename = os.path.join(save_path, "visualization_tree.jpg")
    plt.savefig(visualization_filename)

    ### Save Model
    filename = os.path.join("model", "finalized_model.sav")
    file = open(filename, "wb")
    pickle.dump(model, file)
    file.close()

    ### Prediction
    model_result = model.predict(X_test)

    ### Result
    cm = confusion_matrix(y_test, model_result)
    print("confusion_matrix\n", cm)

    ## Save Confusion Matrix
    plt.figure()
    sns.heatmap(cm, annot = True, linewidths = 0.8, fmt = ".1f")
    plt.title("Confusion Matrix")

    confusion_matrix_filename = os.path.join(save_path, "confusion_matrix.jpg")
    plt.savefig(confusion_matrix_filename)

    report = classification_report(y_test, model_result, output_dict=True)
    print("classification_report\n", report)

    ## Save Classification Report
    plt.figure()
    sns.heatmap(pd.DataFrame(report).iloc[:-1, :].T, annot=True)
    plt.title("Classification Report")
    classification_report_filename = os.path.join(save_path, "classification_report.jpg")
    plt.savefig(classification_report_filename)

if __name__ == "__main__":
    main(sys.argv)









