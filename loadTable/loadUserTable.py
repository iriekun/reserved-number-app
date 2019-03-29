from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Creating your own session
session = boto3.session.Session(profile_name="")
dynamodb = session.resource('dynamodb', region_name='eu-west-1')

table = dynamodb.Table('py-users')

with open("userdata.json") as json_file:
    users = json.load(json_file, parse_float = decimal.Decimal)
    for u in users:
        userId = u['userId']
        role = u['role']
        customerId = u['customerId']

        print("Adding user:", userId, role, customerId)

        table.put_item(
           Item={
               'userId': userId,
               'role' : role,
               'customerId': customerId
            }
        )