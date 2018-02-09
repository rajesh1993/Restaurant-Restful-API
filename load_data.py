from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
# dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Restaurants')

with open("sample_data.json") as json_file:
    restaurants = json.load(json_file, parse_float = decimal.Decimal)
    for rest in restaurants:
        restid = rest['restid']
        restname = rest['restname']
        menu = rest['menu']

        print("Adding restaurant:", restid, restname)

        table.put_item(
           Item={
               'restid': restid,
               'restname': restname,
               'menu': menu,
            }
        )
