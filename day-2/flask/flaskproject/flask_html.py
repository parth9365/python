
from flask import Flask, render_template #importing Flask Library
app = Flask(__name__) #creating and init app flask

@app.route('/') #URL Routing
def hello():	#function for / routing
	return render_template('home.html')

if __name__ == "__main__":	#Defining name as main function
	app.run(debug=True, host='localhost', port=9001)		#starting app
	