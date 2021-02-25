import markovify
import pandas as pd
import json

# linux_rants = pd.read_csv("static/data/linux_rants.tsv", sep='\t')
# linux_rants_model = markovify.NewlineText(linux_rants["mail excerpt"], state_size = 2)
# linux_rants_model.compile()

# for i in range(10):
#     print("-", linux_rants_model.make_sentence())

trump_tweets = pd.read_csv("static/data/trump_insult_tweets_2014_to_2021.csv")
trump_tweets_model = markovify.NewlineText(trump_tweets["tweet"])
trump_tweets_model.compile()

for i in range(10):
    print("-", trump_tweets_model.make_sentence())

# toxic_data = pd.read_pickle("static/data/toxicity_data.pkl")
# toxic_model = markovify.NewlineText(toxic_data["Text"])
# toxic_model.compile()

# for i in range(10):
#     print("-", toxic_model.make_sentence())

# save_toxic_model = toxic_model.to_json()
# with open("static/data/toxicity_data_model.json", "w") as output:
#     json.dump(save_toxic_model, output)