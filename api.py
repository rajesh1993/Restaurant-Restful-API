from __future__ import print_function # Python 2/3 compatibility
import base64
import uuid
import boto3
import json
import simplejson
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from query_get import getRestaurantDetails
from query_delete import deleteRestaurant
from query_insert import addMenu

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

# get a UUID - URL safe, Base64
def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    r_uuid = r_uuid.replace(b'=', b'')
    return bytes.decode(r_uuid)


def abort_if_rest_doesnt_exist(restid):
    # if todo_id not in TODOS:
    abort(404, message="Restaurant {} doesn't exist".format(restid))

parser = reqparse.RequestParser()
parser.add_argument('restid')
parser.add_argument('restname')
parser.add_argument('menuname')
parser.add_argument('menuid')
# RestaurantList
# shows a list of all restaurants, and lets you POST to add new tasks
# class RestaurantList(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201



# Todo
# shows a single todo item and lets you delete a todo item
class Restaurant(Resource):
    def get(self, restid):
        rest_val = getRestaurantDetails(restid)
        if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid) 
        else: return json.dumps(rest_val[0], cls=DecimalEncoder)

    def delete(self, restid):
        rest_val = getRestaurantDetails(restid)
        if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid)
        else: deleteRestaurant(rest_val[0])
        return '', 204
    def post(self, restid):
        rest_val = getRestaurantDetails(restid)
        if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid)
        else: 
            args = parser.parse_args()
            new_menu_id = get_a_uuid()
            restDict = rest_val[0]
            # print(restDict["menu"])
            new_menu = addMenu(restDict["menu"], new_menu_id, args['menuname'], restDict["restid"], restDict["restname"])
            return json.dumps(new_menu, cls=DecimalEncoder), 201

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201


class Menu(Resource):
    def get(self, restid, menuid):
        pass

    def post(self, restid, menuid):
        pass

    def delete(self, rest_id, menuid):
        pass

class Menu_item(Resource):
    def get(self, restid, menuid, itemid):
        pass

    def delete(self, restid, menuid, itemid):
        pass
##
## Actually setup the Api resource routing here
##
# api.add_resource(TodoList, '/rest')
api.add_resource(Restaurant, '/rest/<restid>')


if __name__ == '__main__':
    app.run(debug=True)