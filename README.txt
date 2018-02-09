Hi there!

This is my first attempt at building a REST API.
Since I am most comfortable in python, I looked for resources to build a REST API using any python libraries and I found a gem in Flask.

This REST API will simulate part of an online food ordering system. You will be dealing with the following types of objects:

1. Restaurant
2. Menu
3. Menu Item

Each restaurant can have 0 to many menus associated with it. Each menu can have 0 to many menu items associated with it.

Dependencies: Ensure all of them are installed before proceeding.
Language: Python3
Libraries:
flask
base64
uuid
boto3
json
flask_restful

Database: DynamoDB Local. You can install this from the AWS website. (Ensure that your login credentials are stored in the aws CLI for easy access to the local database.)

We will start by creating a table called 'Restaurants'. To do this run the following command on the terminal after navigating into the folder containing the project files.

python create_db.py

This creates a table on dynamodb local with hash key as 'restid' (Restaurant ID) and sort key as 'restname' (restaurant Name).

Then run

python load_data.py

This will add data from the sample_data.json file into the database.

Run the server by running the following command:

python api.py

This starts the server on localhost.
------------------------------------------------------------------------------------
The classes and their URLs and methods have been listed below. Please note the status at the end of each class and accordingly run tests on the server.
------------------------------------------------------------------------------------


------------------------------------------------------------------------------------
RestaurantList : http://127.0.0.1:5000/rest
------------------------------------------------------------------------------------
Lists all restaurants in the system

Methods:

1. GET - The parent dict is printed out containing all the restaurants

Sample GET structure
[
  {
    "restid": "xSsguRncSSaZumo7JpvAQQ",
    "restname": "McHealthy",
    "menu": [
      {
        "menuid": "0pP1WAz_Eeittv4AxMAVAQ",
        "menuname": "Breakfast",
        "menuitem": [
          {
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
        "menuitem": [
          {
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
  }
]

2. POST - Add a restaurant

Sample POST:
{
   "restname": "SubDay"
}
The restaurant is assigned an ID and created with zero menus (empty menu list)


STATUS - Have not implemented both methods as I have to find out how to acquire all rows of the db (using query/scan and something to do with LastEvaluatedKey as only 1MB of data can be fetched in one pass)
-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Restaurant :  http://127.0.0.1:5000/rest/restid
-------------------------------------------------------------------------------------
List the details of the restaurant with restid.

Methods:

1. GET - Prints the restaurant dict with id = restid

curl -X GET \
  http://localhost:5000/rest/xSsguRncSSaZumo7JpvAQQ\
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 37ec59e5-0787-b0fe-7add-ca116d8419ba' \

Sample GET:
{
    "restid": "xSsguRncSSaZumo7JpvAQQ",
    "restname": "McHealthy",
    "menu": [
      {
        "menuid": "0pP1WAz_Eeittv4AxMAVAQ",
        "menuname": "Breakfast",
        "menuitem": [
          {
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
        "menuitem": [
          {
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
  }

2. POST - Adds a menu to the restaurant and an empty list of menuitem

Sample POST:
{
   "menuname": "Breakfast"
}


3. DELETE - Deletes the Restaurant with restid

STATUS : GET and DELETE work here. POST is yet to be implemented due to the problems that arise in updating dicts in the database. Have to figure that out correctly.
-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Menu : http://127.0.0.1:5000/rest/restid/menuid
-------------------------------------------------------------------------------------
Lists all the items in the menu having menu_id of the restaurant rest_id

Methods:
1. GET - Prints the menu items

curl -X GET \
  http://localhost:5000/rest/xSsguRncSSaZumo7JpvAQQ/0pP1WAz_Eeittv4AxMAVAQ\
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 37ec59e5-0787-b0fe-7add-ca116d8419ba' \

Sample GET:
{
	"menuid": "0pP1WAz_Eeittv4AxMAVAQ",
	"menuname": "Breakfast",
	"menuitem": [
	  {
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
}
2. POST - Adds a menu item to the menuid

Sample POST:
{
   "itemname": "Sandwich"
}

3. DELETE - Deletes the menu having menuid from restid.

STATUS : Only GET implemented due to the dict update problem in DynamoDB.
-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Menu_item : http://127.0.0.1:5000/rest/restid/menuid/itemid
-------------------------------------------------------------------------------------
Lists the item details of the item on menuid of restid.

Methods:
1. GET - Prints the item details.

curl -X GET \
  http://localhost:5000/rest/xSsguRncSSaZumo7JpvAQQ/0pP1WAz_Eeittv4AxMAVAQ/7KFd3Az_Eeir9f4AxMAVAQ \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 37ec59e5-0787-b0fe-7add-ca116d8419ba' \


Sample GET:
{
    "itemid": "2vX-gAz_Eei92f4AxMAVAQ",
    "itemname": "Poached Eggs",
    "itemprice": 100
}


2. DELETE - Deletes the item from the menu.

STATUS: Only GET implemented.

---------------------------------------------------------------------------------------

Pending Tasks:

1. Implement the POST, PUT methods.
2. Create a larger sample database.
3. Unit tests (I'm new to this. I shall learn it soon ;)
4. Record any latency and throughput issues.
4. Scale it on the dynamodb live server and test.
