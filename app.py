from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/scrape")
def scrape():
    mars_insert = mongo.db.mars_insert
    mars_homework = scrape_mars.scrape()
    mars_insert.update({}, mars_homework, upsert=True
    return redirect("http://localhost:5000/", code=302)


@app.route("/")
def index():
    mars_insert = mongo.db.mars_insert.find_one()
    return render_template("index.html", mars_insert = mars_insert)


if __name__ == "__main__":
    app.run(debug=True)