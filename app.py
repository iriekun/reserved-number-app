#!/usr/bin/env python3
from flask import Flask, jsonify, request, Response
from boto3.dynamodb.conditions import Key, Attr

import connexion, json, boto3, decimal

app = Flask(__name__)

# Get dynamodb service resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Numbers') 

def get_numbers_by_customerId(customerId):
    numbers = []
    response = table.query(
        KeyConditionExpression=Key('customerId').eq(customerId)
    )
    items = response['Items']
    print(items)
    for item in items:
        print(item['number'])
        numbers.append(item['number'])
    print(numbers)
    return jsonify(numbers)

# get reserved number list 
@app.route('/reservedNumbers/<userId>')
def get_user_by_id(userId):
    userTable = dynamodb.Table('telenor-users') 
    response = userTable.get_item(
        Key={
            'userId': userId
        }
    )
    item = response['Item']
    role = item['role']
    if (role == "superadmin"):
        customerId = item['customerId']
        return get_numbers_by_customerId(customerId)
    return jsonify({})