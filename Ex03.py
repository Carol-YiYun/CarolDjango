# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:53:17 2024

@author: icesh
"""

from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/news")
def news():
    return render_template("news.html")



app.run() # 執行

