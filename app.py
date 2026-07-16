from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "online_complaint_system"


# Database connection
def get_db():
    return sqlite3.connect("complaint.db")


# Create database tables
def create_tables():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT
    )
    """)

    con.commit()
    con.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Register user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        con = get_db()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(?,?,?)",
            (name, email, password)
        )

        con.commit()
        con.close()

        return redirect("/login")

    return render_template("register.html")


# Login user
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        con = get_db()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cur.fetchone()
        con.close()

        if user:
            session["user"] = user[1]
            return redirect("/dashboard")

    return render_template("login.html")


# Submit complaint
@app.route("/complaint", methods=["GET", "POST"])
def complaint():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        con = get_db()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO complaints(title,description,status) VALUES(?,?,?)",
            (title, description, "Pending")
        )

        con.commit()
        con.close()

        return redirect("/dashboard")

    return render_template("complaint.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    con = get_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM complaints")
    complaints = cur.fetchall()

    con.close()

    return render_template(
        "dashboard.html",
        complaints=complaints
    )


# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
