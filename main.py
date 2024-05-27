# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:02:28 2024

@author: icesh
"""

from flask import request, Flask, render_template
import db
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    sql = "select * from travel order by id desc limit 3"
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    travel = cursor.fetchall()
    
    sql = "select * from goods order by id desc limit 3"
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    goods = cursor.fetchall() # fetchall() 代表抓取查詢出來的全部資料
    
    
    return render_template("index.html", **locals())


@app.route("/product", methods=['GET'])
def goods():
    p = request.args.get('id')
    if p == None:
        sql = "select * from goods order by id desc"
    else: 
        sql = "select * from goods where title like '%{}%' ".format(p)
        # 這是關鍵字搜尋
        
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    result = cursor.fetchall()
        
    return render_template("product.html", result = result )
    

@app.route("/message")
def message():
    return render_template("message.html")

@app.route("/addMsg", methods=['POST'])
def addmessage():
    if request.method == 'POST':
        modify_date = datetime.today()
        mdate = datetime.strftime(modify_date, "%Y-%m-%d")
        
        username = request.form.get('name')
        title = request.form.get('title')
        email = request.form.get('email')
        content = request.form.get('content')
        
        sql = "insert into contact(name, email, subject, content, create_date) values('{}','{}','{}','{}','{}')".format(username, email, title, content, mdate)
        
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        
        
    return render_template("message.html")


@app.route('/display/<int:username>')
def displayName(username):
    if username == 100:
        return "Hello"
    elif username == 200:
        return "Go"
    else:
        sql = "select * from travel order by id desc limit 3"
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        travel = cursor.fetchall()
        
        sql = "select * from goods order by id desc limit 3"
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        goods = cursor.fetchall() # fetchall() 代表抓取查詢出來的全部資料
        
        
        return render_template("index.html", **locals())
    
   # return 'Hello! ' + username


@app.route('/show/<name>')
def show(name):
    return "Hello " + name

@app.route('/two/<one>/<other>')
def showOther(one, other):
    return "Hello " + one + "-" + other




    
if __name__ == "__main__":
    app.debug = True
    app.run()
    
    
    
