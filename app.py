from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
    
def halloheimur():
    return "hallo heimur!!";

