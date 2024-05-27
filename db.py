# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:58:14 2024

@author: icesh
"""

import pymysql

dbsetting = {
    
    "host": "127.0.0.1",
    "port": 3306,
    "user": "lccuser",
    "password":"123456789",
    "db":"lccdemo",
    "charset":"utf8",
    
    
    }


conn = pymysql.connect(**dbsetting)

