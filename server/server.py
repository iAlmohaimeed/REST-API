#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self, employee_name):
        ''' GET REQUEST HANDLER FOR /employee/<employee_name> ENDPOINT '''
        return employee_name

    def post(self, employee_name):
        ''' POST REQUEST HANDLER FOR /employee/<employee_name> ENDPOINT '''
        return True

'''
        ---- THE LIST OF ENDPOINTS ---- 
    Syntax:
    api.add_resource(ClassName, '/endpointName/<parameter>')
'''
api.add_resource(Employee, '/employee/<employee_name>')  # Endpoint #1

if __name__ == '__main__':
    app.run()
