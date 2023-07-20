from sqlite3.dbapi2 import connect
from flask import Flask, json, request
from flask_restful import Resource, Api
import sqlite3
import json

app = Flask(__name__)
api = Api(app)

# first_run = input("First time run the program? (yes/no): ").strip()
# if first_run == "yes":
#     conn = sqlite3.connect("PC_Store_DB.db")
#     curr = conn.cursor()
#     curr.execute('create table PC(pc_ID int primary key, CPU varchar(50), RAM int, SSD varchar(50), price int)')
#     curr.execute('drop table Customer;')
#     curr.execute('''create table Customer( 
#                             CustomeID int primary key,
#                             Name varchar(30), 
#                             Surname varchar(30), 
#                             email varchar(40), 
#                             pc_ID int, 
#                             foreign key(pc_ID) references PC(pc_ID) on update cascade on delete set null)
#                         ''')
    # curr.execute('PRAGMA foreign_keys = OFF;')
#     # curr.execute('alter table Customer foreign key(pc_ID) references PC(pc_ID);')
#     conn.commit()
#     conn.close()
# else:
#     conn = sqlite3.connect("PC_Store_DB.db")
#     curr = conn.cursor()
#     tables = curr.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     print(tables.fetchall())
#     print(curr.execute('PRAGMA table_info(PC)').fetchall())
#     conn.close()


class Customer(Resource):
    def post(self):
        data = json.loads(request.form['data'])
        print(data)
        conn = sqlite3.connect("PC_Store_DB.db")
        curr = conn.cursor()
        try:
            curr.execute('''
                insert into Customer 
                values
                (?, ?, ?, ?, ?)
            ''', (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()
            conn.close()
            return {"success_msg": "New customer successfully added!"}
        except:
            conn.commit()
            conn.close()
            return {"error" : "Insertion did not succeed. Please make sure you inserted all the data with appropriate data types."}
        

    def delete(self, customerID):
        conn = sqlite3.connect("PC_Store_DB.db")
        curr = conn.cursor()
        try:
            curr.execute('''
                delete from Customer where CustomerID = ?
            ''', (customerID))
            return {"success_msg": "Customer successfully deleted!"}
        except:
            return {"error" : "Deleting a customer did not succeed. Please make sure you inserted an existing user ID."}


class PCstore(Resource):
    def post(self):
        data = json.loads(request.form['data'])
        print(data)
        conn = sqlite3.connect("PC_Store_DB.db")
        curr = conn.cursor()
        try:
            curr.execute('''
                insert into PC 
                values
                (?, ?, ?, ?, ?)
            ''', (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()
            conn.close()
            return {"success_msg": "New pc successfully added!"}
        except:
            conn.commit()
            conn.close()
            return {"error" : "Insertion did not succeed. Please make sure you inserted all the data with appropriate data types."}
    def delete(self, pc_id):
        conn = sqlite3.connect("PC_Store_DB.db")
        curr = conn.cursor()
        try:
            curr.execute(f'''delete from PC where pc_ID = {pc_id}''')
            conn.commit()
            return {"success_msg": "PC successfully deleted!"}
        except:
            return {"error" : "Deleting a PC did not succeed. Please make sure you inserted an existing item ID."}
    

api.add_resource(Customer, "/", "/customers/<int:customerID>")
api.add_resource(PCstore, "/add_pc", "/remove_pc/<int:pc_id>")

if __name__ == "__main__":
    app.run(debug=True)
