from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Restaurants')

# restid =  "xSsguRncSSaZumo7JpvAQQ"
# restname = "McHealthy"
# response = table.query(KeyConditionExpression=Key('restid').eq(restid))
# new_menu = {"menuid": "Asf3fsdvxSsguRncSS",
#             "menuname": "Brunch",
#             "menuitem": []}
# print(response)
# menu = response['Items'][0]["menu"]
# if menu != None: updated_menu = menu.append(new_menu)
# else: updated_menu = new_menu
# response = table.update_item(
#     Key={
#         'restid': restid,
#         'restname': restname
#     },
#     UpdateExpression="set menu=:m",
#     ExpressionAttributeValues={
#         ':m': updated_menu
#     },
#     ReturnValues="UPDATED_NEW"
# )
# print("PutItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))




def addMenu(menu, new_menuID, new_menuName, restid, restname):
    print("old_menu is ", menu)
    new_menu = {"menuid": new_menuID,
                "menuname": new_menuName,
                "menuitem": []}
    if menu != None: updated_menu = menu.append(new_menu)
    else: updated_menu = new_menu
    response = table.update_item(
        Key={
            'restid': restid,
            'restname': restname
        },
        UpdateExpression="set menu=:m",
        ExpressionAttributeValues={
            ':m': updated_menu
        },
        ReturnValues="UPDATED_NEW"
    )
    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))
    return new_menu