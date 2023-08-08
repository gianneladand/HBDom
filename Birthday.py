import time
from flask import Flask, render_template, request

app = Flask("Birthday Gift Picker")

options = [
    "iPhone 15",
    "Play 5",
    "Trip to a Private Island",
    "Tickets for Tomorrowland",
    "Gamer PC",
    "Skydiving",
    "New car",
    "Trip to Disney",
    "Helicopter Tour",
    "Free KFC for 5 years",
    "Selecting..."
]

fixed_option = "a massage"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pick_random")
def pick_random():
    return render_template("random_result.html", option=fixed_option)

@app.route("/simulate", methods=["GET", "POST"])
def simulate():
    if request.method == "POST":
        return render_template("simulate.html", options=options)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
