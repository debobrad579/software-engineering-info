from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html", active="home")


@app.route("/my-journey")
def my_journey():
    return render_template("my-journey.html", active="my-journey")


if __name__ == "__main__":
    app.run(debug=True)
