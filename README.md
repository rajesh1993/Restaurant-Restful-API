Restaurant

r_id
r_name
r_address
r_cuisine
[menu_id]
r_contact
r_email

Menu
m_id
m_type
page_count
[menu_item_id]

Menu Item
item_id
item_name
price

------------------------------------------------------------------------------------
Restaurant_List : http://127.0.0.1:5000/rest
------------------------------------------------------------------------------------
Lists all restaurants in the system

Methods:

1. GET - The parent dict is printed out containing all the restaurants

Sample GET structure
[{
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

2. POST - Add a restaurant

Sample POST:
{
   "restname": "SubDay"
}
The restaurant is assigned an ID and created with zero menus (empty menu list)

-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Restaurant :  http://127.0.0.1:5000/rest/restid
-------------------------------------------------------------------------------------
List the menus associated with restaurant rest_name

Methods:

1. GET - Prints the menu dict of the restaurant
Sample GET:
{
	"restid" : 1,
	"restname": "McHealthy",
	"menu":[
				{
					"menuid": 1
					"menuname": "Breakfast",
					"menuitem":[
									{
										"itemid": 1,
										"itemname": "Poached Eggs",
										"itemprice": 100
									},
									{
										"itemid": 2,
										"itemname": "Cereal",
										"itemprice": 50
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
-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Menu : http://127.0.0.1:5000/rest/restid/menuid
-------------------------------------------------------------------------------------
Lists all the items in the menu having menu_name of the restaurant rest_id

Methods:
1. GET - Prints the menu items

Sample GET:
{
	"menuid": 1
	"menuname": "Breakfast",
	"menuitem":[
					{
						"itemid": 1,
						"itemname": "Poached Eggs",
						"itemprice": 100
					},
					{
						"itemid": 2,
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
-------------------------------------------------------------------------------------
#######################################################################################
-------------------------------------------------------------------------------------
Menu_item : http://127.0.0.1:5000/rest/restid/menuid/itemid
-------------------------------------------------------------------------------------
Lists the item details of the item on menuid of restid.

Methods:
1. GET - Prints the item details.

Sample GET:
{
	"itemid": 1,
	"itemname": "Poached Eggs",
	"itemprice": 100
}


2. DELETE - Deletes the item from the menu.





