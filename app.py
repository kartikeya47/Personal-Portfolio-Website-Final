from flask import Flask, render_template, request, redirect
import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

firebaseConfig = {'apiKey': os.getenv('apiKey'),
  'authDomain': os.getenv('authDomain'),
  'projectId': os.getenv('projectId'),
  'storageBucket': os.getenv('storageBucket'),
  'messagingSenderId': os.getenv('messagingSenderId'),
  'appId': os.getenv('appId'),
  'measurementId': os.getenv('measurementId'),
  'databaseURL': os.getenv('databaseURL')}

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