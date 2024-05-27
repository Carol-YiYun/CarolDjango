# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:48:49 2024

@author: icesh
"""

from flask import Flask

app = Flask(__name__)

@app.route("/news")
def news():
    return "這是新聞頁"


@app.route("/product")
def goods():
    return "這是產品頁"



app.run() # 執行