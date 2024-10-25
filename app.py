from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def login():
  return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
  username = request.form.get("username")
  password = request.form.get("password")
  role = request.form.get("role")

  if username and password and role:
    return redirect(url_for("home"))
  else:
    return redirect(url_for("/login"))


@app.route("/emergency")
def emergency():
  return render_template("emergency.html")


@app.route("/submit_emergency", methods=["POST"])
def handle_emergency():
  patient_name = request.form.get("patient_name")
  condition = request.form.get("condition")
  location = request.form.get("location")

  if patient_name and condition and location:
    return redirect(url_for("home"))
  else:
    return redirect(url_for("emergency"))


@app.route("/home")
def home():
  return render_template("home.html")


if __name__ == "__main__":
  app.run()
