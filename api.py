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

# Helper to access nested dicts
class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)

            if not val:
                break;

        return val

# get a UUID - URL safe, Base64
def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    r_uuid = r_uuid.replace(b'=', b'')
    return bytes.decode(r_uuid)


def abort_if_rest_doesnt_exist(restid):
    # if restid not in database:
    abort(404, message="Restaurant {} doesn't exist".format(restid))

def abort_if_menu_doesnt_exist(menuid):
    # if menuid not in database:
    abort(404, message="Menu {} doesn't exist".format(restid))

def abort_if_menu_item_doesnt_exist(itemid):
    # if itemid not in database:
    abort(404, message="Menu Item {} doesn't exist".format(itemid))

# Add arguments to expect from the command line
parser = reqparse.RequestParser()
parser.add_argument('restid')
parser.add_argument('restname')
parser.add_argument('menuname')
parser.add_argument('menuid')
# RestaurantList
# shows a list of all restaurants, and lets you POST to add new tasks
class RestaurantList(Resource):
    def get(self):
        # Show all restaurants here or ten at a time or whatever works
        pass

    def post(self):
        #Add a restaurant here by generating a UUID and accepting name of
        #restaurant by POST
        pass


# shows a single restaurant
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

    # need to implement post to add a menu to the restaurant
    def post(self, restid):
        pass
    # def post(self, restid):
    #     rest_val = getRestaurantDetails(restid)
    #     if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid)
    #     else: 
    #         args = parser.parse_args()
    #         new_menu_id = get_a_uuid()
    #         restDict = rest_val[0]
    #         new_menu = addMenu(restDict["menu"], new_menu_id, args['menuname'], restDict["restid"], restDict["restname"])
    #         return json.dumps(new_menu, cls=DecimalEncoder), 201

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

# Shows the menu if a given restaurant
class Menu(Resource):
    def get(self, restid, menuid):
        rest_val = getRestaurantDetails(restid)
        if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid) 
        else:
            menu = rest_val[0]["menu"]
            for item in menu:
                if item["menuid"] == menuid: 
                    return json.dumps(item["menuid"], cls=DecimalEncoder)
            abort_if_menu_doesnt_exist(menuid)
    # Implement a menthod to add a menu item to the given menu
    def post(self, restid, menuid):
        pass
    # Implement a method to delete a menu
    def delete(self, rest_id, menuid):
        pass


# Shows the items on a menu
class Menu_item(Resource):
    def get(self, restid, menuid, itemid):
        rest_val = getRestaurantDetails(restid)
        if rest_val == -1 or rest_val == []: abort_if_rest_doesnt_exist(restid) 
        else:
            menu = rest_val[0]["menu"]
            for item in menu:
                if item["menuid"] == menuid: 
                    for menu_item in item["menuitem"]:
                        if menu_item["itemid"] == itemid:
                            return json.dumps(menu_item, cls=DecimalEncoder)
            abort_if_menu_item_doesnt_exist(itemid)
    
    # Implement a method to delete a menu item
    def delete(self, restid, menuid, itemid):
        pass
##
## Actually setup the Api resource routing here (endpoints)
##
api.add_resource(Restaurant, '/rest/<restid>')
api.add_resource(Menu, '/rest/<restid>/<menuid>')
api.add_resource(Menu_item, '/rest/<restid>/<menuid>/<itemid>')

# Runs the app on the local server
if __name__ == '__main__':
    app.run(debug=True)