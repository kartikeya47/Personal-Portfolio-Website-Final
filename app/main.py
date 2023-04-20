from flask import Flask, render_template, request, redirect
import pyrebase

app = Flask(__name__)

firebaseConfig = {'apiKey': "AIzaSyBRyj1YZYpWwSffmxuZH8Td5-OQI5zhVCM",
  'authDomain': "personalportfoliowebapp.firebaseapp.com",
  'projectId': "personalportfoliowebapp",
  'storageBucket': "personalportfoliowebapp.appspot.com",
  'messagingSenderId': "506312845182",
  'appId': "1:506312845182:web:cb778ed2b86e4c238ef52f",
  'measurementId': "G-QZKF8SVLS7",
  'databaseURL': "https://personalportfoliowebapp-default-rtdb.firebaseio.com/"}

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