from flask import Flask, request, jsonify, make_response, render_template
import time
import pickle
import pandas as pd
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import MinMaxScaler

# from flask_restful import Resource, Api;
# from marshmallow import fields;
# from marshmallow_sqlalchemy import ModelSchema;

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", send_range="0.00")


# create krnw end point
@app.route("/form_to_app_py", methods=["POST"])
def post_request_function():

    vote = request.form.get("vote")
    avg = request.form.get("avg")
    price = request.form.get("price")
    table = request.form.get("table")
    delivery = request.form.get("delivery")

    model_range = "Please select data for access rating ..."

    if vote:
        if avg:
            if price:
                if table:
                    if delivery:
                        model_range = str(
                            predictFunction(vote, avg, table, delivery, price)
                        )
                        time.sleep(2)

    return render_template("index.html", send_range=model_range)


def predictFunction(vote, avg, table, delivery, price):
    Predictors = [
        "Votes",
        "Average_Cost_for_two",
        "Has_Table_booking",
        "Has_Online_delivery",
        "Price_range",
    ]
    # new_samples_data=pd.DataFrame(data=[[591,1200,1,0,3],[10,4000,1,0,4]],columns=Predictors);
    # function eke parameeter valuetik damma
    new_samples_data = pd.DataFrame(
        data=[[vote, avg, table, delivery, price]], columns=Predictors
    )
    model = pickle.load(open("model.pkl", "rb"))
    result = model.predict(new_samples_data)
    # print(result);
    return result


if __name__ == "__main__":
    app.run(debug=True)
