from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
# dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.create_table(
    TableName='Restaurants',
    KeySchema=[
        {
            'AttributeName': 'restid',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'restname',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'restid',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'restname',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)

print("Table status:", table.table_status)
