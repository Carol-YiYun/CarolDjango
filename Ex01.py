# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:38:25 2024

@author: icesh
"""

# 宣告使用 flask
from flask import Flask

# 初始化 flask 物件
app = Flask(__name__)

# 建立主網址的路徑 / => 根目錄（可以自訂）
# @app.route 要對應一個函數，ex: home
@app.route("/")

def home():
    return "這是首頁"


app.run() # 執行




