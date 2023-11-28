import mysql.connector
from mysql.connector import Error
import os

class dbadapt:  
         
     def retrieve():
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="watersys"
        )
        cursor = connection.cursor()
        print("connected")
        #select_query = "SELECT * FROM users"
        #cursor.execute(select_query)
        #infor=[]
        #while True:
        #    print("searching")
         #   result = cursor.fetchone()
          #  infor.append(result)
           # if result==None:
           #     break
        #print(infor)
        #print("retrive succesful")
        #cursor.close()
        connection.close()
        #return infor
        
     def store():
        connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
        )
        try:
            cursor = connection.cursor()
            add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")
            add_salary = ("INSERT INTO salaries "
                "(emp_no, salary, from_date, to_date) "
                "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
            data= ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
            cursor.execute(add_employee, data)
        except Error:
            print("error emcountered")
        finally:
            cursor.close()
            connection.close()
            
            
     def select():
        connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
        )
        cursor = connection.cursor()
        select_query = "SELECT location FROM users"
        cursor.execute(select_query)
        infor=[]
        while True:
            result = cursor.fetchone()
            infor.append(result)
            if result==None:
                break
        print(infor)
        print("retrive succesful")
        cursor.close()
        connection.close()
        return infor
    
     def search(stuff):
        connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
        )
        cursor = connection.cursor()
        select_query = "SELECT * from pple WHERE Name= (?)"
        cursor.execute(select_query, (stuff,))
        infor=[]
        while True:
            result = cursor.fetchone()
            infor.append(result)
            if result==None:
                break
        print(infor)
        print("retrive succesful")
        cursor.close()
        connection.close()
        return infor
        
        
        
            
            
            
            
            
if __name__ == "__main__":
    dbadapt.retrieve()