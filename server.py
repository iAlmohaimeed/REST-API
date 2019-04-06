#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        ''' Get a list of employees ID '''
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
    def post(self):
        ''' Add a new employee to the DB'''
        conn = db_connect.connect() #1

        print(request.json)
        LastName = request.json['LastName'] #2
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']

        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName,FirstName,Title,
                             ReportsTo, BirthDate, HireDate, Address,
                             City, State, Country, PostalCode, Phone, Fax,
                             Email)) #3 
        return {'status':'success'}

    
class Tracks(Resource):
    def get(self):
        conn = db_connect.connect() #1
        query = conn.execute("select trackid, name, composer, unitprice from tracks;") #2
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} #3
        return jsonify(result)

    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect() #1
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id)) #2
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} #3
        return jsonify(result)

class Remove_Employee(Resource):
    def get(self, employee_id):
        ''' Delete employee from DB'''
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        return {'status':'success'}

'''
    ---- THE LIST OF ROUTES FOR THE API ----
'''
api.add_resource(Employees, '/employees') # Route_1: List number of employees
api.add_resource(Tracks, '/tracks') # Route_2: Display tracks info. 
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3: Display an employee info. 
api.add_resource(Remove_Employee, '/removeemployees/<employee_id>') # Route_4: Remove an employee from DB


if __name__ == '__main__':
     app.run()
