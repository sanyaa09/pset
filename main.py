from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import random
#from finance import fetch_data

# initializing our app
app = Flask(__name__)


# telling flask to call hello() when "/" called on browser
@app.route("/")
def hello():
    return render_template('index.html')


# when form is submitted data is sent to this url
# following function handles it
# it goes here because we set it in action param in form tag
@app.route("/symbol", methods = ['POST'])
def get_symbol():
    # getting symbol from response
    symbol = request.form['symbol']

    # calling a function that you will write
    data = fetch_data(symbol)

    # handle if data is None return error
    # render data otherwise
    if data is None:
        return redirect('/error', code=302)
    else:
        return render_template('data.html', items=data)



@app.route("/error")
def error():
    errors = [':<', ':{', ':(', ':[', '):', '>:', '}:', ']:']
    return 'error ' + random.choice(errors)


# running our app
# debug=True reloads server whenever you save file
# so you dont have to mannualy restart every time
app.run(debug=True)