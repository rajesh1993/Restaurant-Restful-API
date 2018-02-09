from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

'''
Routes can use different converters in their definition,

@app.route('/articles/<articleid>')
Can be replaced by

@app.route('/articles/<int:articleid>')
@app.route('/articles/<float:articleid>')
@app.route('/articles/<path:articleid>')
The default is string which accepts any text without slashes.

'''

@app.route('/articles')
def api_articles():
	return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
	return 'You are reading ' + articleid

'''
GET /
Welcome

GET /articles
List of /articles

GET /articles/123
You are reading 123
'''

#------------------GET parameters-----------------------

from flask import request

@app.route('/hello')
def api_hello():
	if 'name' in request.args:
		return 'Hello ' + request.args['name']
	else:
		return 'Hello John Doe'

#--------------------Request Methods (HTTP Verbs)------------
#curl -X PATCH http://127.0.0.1:5000/echo
#Use the above to test

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
	if request.method == 'GET':
		return "ECHO: GET\n"
	elif request.method == 'POST':
		return "ECHO: POST\n"
	elif request.method == 'PATCH':
		return "ECHO: PATCH\n"
	elif request.method == 'PUT':
		return "ECHO: PUT\n"	
	elif request.method == 'DELETE':
		return "ECHO: DELETE\n"


#---------------------Request Data & Headers-------------------
from flask import json
@app.route('/messages', methods = ['POST'])
def api_message():
	if request.headers['Content-Type'] == 'text/plain':
		return "Text Message: " + request.data
	elif request.headers['Content-Type'] == 'application/json':
		rest_name = request.get_json()
		return "The restaurant is called " + rest_name['Restaurant'] \
		+ " and it serves " + rest_name['Menu']['Type'][0]
		# return "JSON Message: \n" + json.dumps(request.json)
	else:
		return "415 Unsupported Media Stream Type"







if __name__ == '__main__':
	app.run(debug=True)