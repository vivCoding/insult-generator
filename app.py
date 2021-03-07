from flask import Flask, render_template, jsonify, make_response
import init_markov
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

model = init_markov.get_model()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/getinsult")
def get_insult():
    return jsonify(model.make_sentence()), 200

if __name__ == "__main__":
    app.run(debug=False)