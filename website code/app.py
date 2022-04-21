from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("bot.html")
    
if __name__ == "__main__":
    app.run(debug=True)