from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['get','post'])
def home():
    return render_template('index.html')

from controller import *
