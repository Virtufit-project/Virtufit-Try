from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "virtufit_secret"

def get_db():
    return sqlite3.connect("database/app.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# 👕 صفحة تجربة الملابس الافتراضية
@app.route("/tryon")
def tryon():
    return render_template("tryon.html")

if __name__ == "__main__":
    app.run(debug=True)
