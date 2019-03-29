from __future__ import print_function # Python 2/3 compatibility
import boto3

# create your own session
session = boto3.session.Session(profile_name="")
dynamodb = session.resource('dynamodb', region_name='eu-west-1')

table = dynamodb.create_table(
    TableName='py-numbers',
    
    KeySchema=[
        {
            'AttributeName': 'customerId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'number',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'customerId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'number',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)