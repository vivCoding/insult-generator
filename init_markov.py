import markovify
import pandas as pd
import json

SAVED_MODEL = "static/data/all_insults.json"

def model_txt(path):
    with open(path, "r") as f:
        text = f.read()
    model = markovify.Text(text, state_size=2)
    return model

def model_csv(path, column, sep=","):
    df = pd.read_csv(path, sep=sep)
    model = markovify.Text(df[column], state_size=2)
    return model

def create_model():
    # create models from file datasets
    general_insults = model_txt("static/data/corpus.txt")
    more_insults = model_csv("static/data/final.csv", "Comment")
    linux_rants = model_csv("static/data/linux_rants.tsv", sep="\t", column="mail excerpt")

    # combine models and save to json file
    combined_model = markovify.combine([general_insults])
    combined_model.compile()
    combined_model = combined_model.to_json()
    with open(SAVED_MODEL, "w") as output:
        json.dump(combined_model, output)

def get_model():
    with open(SAVED_MODEL, "r") as f:
        data = f.read()
    data = json.loads(data)
    model = markovify.Text.from_json(data)
    return model

create_model()
model = get_model()
print(model.make_sentence())