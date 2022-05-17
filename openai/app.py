import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest 10 names of big animals in a list.
1.Animal: {}
.Animal:""".format(
        animal.capitalize()
    )
