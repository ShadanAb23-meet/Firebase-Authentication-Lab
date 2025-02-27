from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {

  "apiKey": "AIzaSyAEKzs6me3O7YGSPpVQGYcKpHO3McROsrI",

  "authDomain": "authentication-2e1b9.firebaseapp.com",

  "projectId": "authentication-2e1b9",

  "storageBucket": "authentication-2e1b9.appspot.com",

  "messagingSenderId": "1005608705490",

  "appId": "1:1005608705490:web:ce2b333b88ebac2ab37c0b",

  "measurementId": "G-EYC7Q8BH6C",
  "databaseURL": "https://authentication-2e1b9-default-rtdb.europe-west1.firebasedatabase.app/"

}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
app=Flask(__name__)


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session["user"]= auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
			return render_template("signin.html")
	return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
	try:
		login_session["user"]= auth.create_user_with_email_and_password(email, password)
		return redirect(url_for('add_tweet'))
	except:
		error = "Authentication failed"
		return render_template("signup.html")

	return render_template("signup.html")




@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
	return render_template("add_tweet.html")


if __name__ == '__main__':
	app.run(debug=True)