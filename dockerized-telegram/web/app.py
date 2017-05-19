# -*- coding: utf-8 -*-
from flask import Flask,make_response,render_template,request
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/")
def index():
    db=MongoClient('db')
    client = db.telegram
    fetcher  = client.telegramcollection
    return render_template("index.html",datas=fetcher.find())
