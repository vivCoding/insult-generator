import markovify
import pandas as pd
df = pd.read_csv("rants.tsv", sep='\t')
#df = df["mail excerpt"]
# text = ""
# for index, row in df.iterrows():
#     text = text + (row["mail excerpt"])

# Get raw text as string.
# with open("/path/to/my/corpus.txt") as f:
#     text = f.read()
#
# Build the model.
text_model = markovify.NewlineText(df["mail excerpt"], state_size = 2)

# # Print five randomly-generated sentences
# for i in   print(text_model.make_sentence()) range(5):


# Print three randomly-generated sentences of no more than 280 characters
for i in range(10):
    print(text_model.make_sentence())