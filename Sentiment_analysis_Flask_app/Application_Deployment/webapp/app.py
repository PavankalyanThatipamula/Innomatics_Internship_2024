from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from preprocessing import lowers_text, special_char, Digits, lemma


##############

app = Flask(__name__)

##############
@app.route("/")
def index():
    return render_template("home.html")


#########
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import pickle

# Create the pipeline
Pre_process_pip = Pipeline([
    ('Lower', FunctionTransformer(lowers_text, validate=False)),
    ('Digits', FunctionTransformer(Digits, validate=False)),
    ('Special_characters', FunctionTransformer(special_char, validate=False)),
    ('Advance', FunctionTransformer(lemma, validate=False))
])

##########

@app.route("/Prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        Text = request.form.get("text")
        Review = pd.Series(Text)

        Model = pickle.load(open(r"models\best_model.pkl", 'rb'))
        

        predicted_sentiment = Model.predict(Pre_process_pip.transform(Review))

        # Map predicted sentiment to human-readable labels
        predicted_sentiment_label = "Positive" if predicted_sentiment[0] == 1 else "Negative"

    return render_template("prediction_form.html", predicted_sentiment_label=predicted_sentiment_label)


##############


if __name__ == '__main__':
    app.run(debug=True,host ='0.0.0.0')