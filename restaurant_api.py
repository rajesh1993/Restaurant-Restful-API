from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

RESTAURANTS = [{
    "restid": "xSsguRncSSaZumo7JpvAQQ",
    "restname": "McHealthy",
    "menu": [{
            "menuid": "0pP1WAz_Eeittv4AxMAVAQ",
            "menuname": "Breakfast",
            "menuitem": [{
                    "itemid": "2vX-gAz_Eei92f4AxMAVAQ",
                    "itemname": "Poached Eggs",
                    "itemprice": 100
                },
                {
                    "itemid": "7KFd3Az_Eeir9f4AxMAVAQ",
                    "itemname": "Cereal",
                    "itemprice": 50
                }
            ]
        },
        {
            "menuid": "9hHBNgz_EeiC8P4AxMAVAQ",
            "menuname": "Lunch",
            "menuitem": [{
                    "itemid": "avILqAz_EeiyDv4AxMAVAQ",
                    "itemname": "Lasagna",
                    "itemprice": 200
                },
                {
                    "itemid": "CHsRYg0AEeicav4AxMAVAQ",
                    "itemname": "Pasta",
                    "itemprice": 250
                }
            ]
        }
    ]
}]

def abort_if_rest_doesnt_exist(rest_id):
    if rest_id not in RESTAURANTS:
        abort(404, message="Restaurant {} doesn't exist".format(rest_id))

parser = reqparse.RequestParser()
parser.add_argument('rest')


# Todo
# shows all menus for one restaurant and lets you delete a menu
class Menu(Resource):
    # Prints out all menus associated with restaurant rest_id
    def get(self, rest_id):
        abort_if_rest_doesnt_exist(rest_id)
        return RESTAURANTS[rest_id]
    # Deletes the restaurant with rest_id
    def delete(self, rest_id):
        abort_if_rest_doesnt_exist(rest_id)
        del RESTAURANTS[rest_id]
        return '', 204
    # Updates the restaurant with rest_id
    def put(self, rest_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all res, and lets you POST to add new tasks
class RestList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(RestList, '/rest')
api.add_resource(Menu, '/todos/<rest_id>')


if __name__ == '__main__':
    app.run(debug=True)