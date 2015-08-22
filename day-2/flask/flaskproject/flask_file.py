from flask import Flask #importing Flask Library
app = Flask(__name__) #creating and init app flask

@app.route('/') #URL Routing
def hello():	#function for / routing
	return "Hello World!"	#Returning 'Hello World!' on / route

@app.route('/foo')
def foo():
	return 'Hello Foo!'

if __name__ == "__main__":	#Defining name as main function
	app.run()		#starting app
	