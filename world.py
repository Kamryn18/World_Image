from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def homepage():
    svg = open('monica.svg').read
    return render_template("world.html", svg=svg)

app.run(debug=True)
