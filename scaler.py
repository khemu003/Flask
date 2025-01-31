from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
app = Flask(__name__)

@app.route("/StandardScaler/")
def scaler():
    df = pd.read_csv("D:\\DataSet\\placement.csv")
    
    df.isnull().sum()
    df.dropna()

    x = df.drop(columns = ["placed"])
    y = df["placed"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    sc = StandardScaler()

    x_train_sc = sc.fit_transform(x_train)

    x_train_sc_df = pd.DataFrame(x_train_sc, columns=x_train.columns)

    output = np.round(x_train_sc_df.describe(), 1)

    result = {
        "Dataset" : "placement.csv",
        "Scaler" : "StandardScaler",
        "output" : "StandardScaler is successful run!",
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug= True)