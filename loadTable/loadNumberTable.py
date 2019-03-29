from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Creating your own session
session = boto3.session.Session(profile_name="")
dynamodb = session.resource('dynamodb', region_name='eu-west-1')

table = dynamodb.Table('py-numbers')

with open("numberdata.json") as json_file:
    numbers = json.load(json_file, parse_float = decimal.Decimal)
    for num in numbers:
        number = str(num['number'])
        customerId = str(num['customerId'])

        print("Adding number:", number, customerId)

        table.put_item(
           Item={
               'number': number,
               'customerId': customerId
            }
        )