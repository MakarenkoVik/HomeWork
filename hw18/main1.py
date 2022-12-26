#!.venv/bin/python
from flask import Flask
from datetime import datetime

app = Flask(__name__) 

@app.route("/time") 
def time():
    current_time = str(datetime.now().time())
    return current_time
