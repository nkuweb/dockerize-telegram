# -*- coding: utf-8 -*-
from flask import Flask,make_response,render_template,request
from pymongo MongoClient
app = Flask(__name__)
db=MongoClient('db')
@app.route("/")
def index():
    datas=["hello","world","I","love","everyone"]
    return render_template("index.html",datas=datas)


app.run(debug=True,host='0.0.0.0')
