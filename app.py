from flask import Flask, render_template, request, redirect
import pyrebase
import os

apiKey = os.environ.get('apiKey')
authDomain = os.environ.get('authDomain')
projectId = os.environ.get('projectId')
storageBucket = os.environ.get('storageBucket')
messagingSenderId = os.environ.get('messagingSenderId')
appId = os.environ.get('appId')
measurementId = os.environ.get('measurementId')
databaseURL = os.environ.get('databaseURL')

app = Flask(__name__)

firebaseConfig = {'apiKey': apiKey,
  'authDomain': authDomain,
  'projectId': projectId,
  'storageBucket': storageBucket,
  'messagingSenderId': messagingSenderId,
  'appId': appId,
  'measurementId': measurementId,
  'databaseURL': databaseURL}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        data = {'name': name, 'email': email, 'subject': subject, 'message': message}
        db.child(name).set(data)
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()