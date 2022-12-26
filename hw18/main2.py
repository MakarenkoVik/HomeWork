#!.venv/bin/python
from flask import Flask
import requests

app = Flask(__name__) 

@app.route("/quote") 
def quote():
    quote = requests.get("https://api.kanye.rest").json()
    return quote["quote"]
