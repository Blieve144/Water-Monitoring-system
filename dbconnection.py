import sqlite3
from random import random

class adaptor():
    def retrive_all():
        db = sqlite3.connect('watersys.db')
        sql = "SELECT * from water;"
        cur = db.cursor()
        cur.execute(sql)
        source = []
        while True:
            record = cur.fetchone()
            source.append(record)
            if record == None:
                break
        print(source)
        print("retrive succesful")
        return source
        
        
        
    def storecomplaint(userid,waterid,watername,complaint,approxdanger):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            complaintid= random(0,100000)
            data = (complaintid,userid,waterid,watername,complaint,approxdanger)
            print("gotten data")
            sql = """INSERT INTO complaint (complaintid,userid,waterid,name,complaint,approxdanger) VALUES (?,?,?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
            
    def search(sname,password):
        db = sqlite3.connect('watersys.db')
        sql = "SELECT * from User WHERE name= (?) AND Password= (?)"
        cur = db.cursor()
        cur.execute(sql, (sname,password,))
        names = []
        while True:
            record = cur.fetchone()
            names.append(record)
            if record == None:
                break
        print(names)
        return names
    
    
    def select():
        db = sqlite3.connect('watersys.db')
        sql = """SELECT name from user"""
        cur = db.cursor()
        cur.execute(sql)
        names1 = []
        while True:
            record = cur.fetchone()
            names1.append(record)
            if record == None:
                break
        print(names1)
        return names1
    
    
