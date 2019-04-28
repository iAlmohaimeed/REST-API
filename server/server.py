#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class Employee(Resource):
    def get(self, employee_name):
        ''' GET REQUEST HANDLER FOR /employee/<employee_name> ENDPOINT '''
        return 1
    
    def post(self, employee_name):
        ''' POST REQUEST HANDLER FOR /employee/<employee_name> ENDPOINT '''
        return employee_name

    
class Job(Resource):
    def get(self, employee_id):
        ''' GET REQUEST HANDLER FOR /jobs/<employee_id> ENDPOINT '''
        return 1

    def post(self, employee_id):
        ''' POST REQUEST HANDLER FOR /jobs/<employee_id> ENDPOINT '''
        return 1

'''
        ---- THE LIST OF ENDPOINTS ---- 
    Syntax:
    api.add_resource(ClassName, '/endpointName')
'''
api.add_resource(Employee, '/employee/<employee_name>') # Endpoint #1
api.add_resource(Job, '/jobs/<employee_id>') # Endpoint #2


if __name__ == '__main__':
     app.run()
