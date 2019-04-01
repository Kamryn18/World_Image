from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def homepage():
    svg = open('world.svg').read
    return render_template("world.html", svg=Markup(svg))

app.run(debug=True)
