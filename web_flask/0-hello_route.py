#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
