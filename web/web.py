# -*- coding: utf-8 -*-
from flask import Flask,make_response,render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1 style=margin-left:20em;margin-top:20em;>Hayırsız Leylaa...</h1>"
app.run(debug=True,host='0.0.0.0')
