import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
# This line is strictly required for Vercel deployment
app.debug = False

@app.route('/')
def home():
    return render_template('index.html')

# Vercel needs 'app' object globally accessible
