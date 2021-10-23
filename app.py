""" Flask application that runs the API and renders the html page(s) """
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

######## Setting up the Flask app ########
# Spin up flask app
app = Flask(__name__)

# Add the connection to the sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = "YOUR CONNECTION STRING HERE"
# This just ensures that the app runs more quickly
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Get the db instance
db = SQLAlchemy(app)

# Table classes which are based on db schema
class ItemInfo(db.Model):
    __tablename__ = "item_info"
    unique_id = db.Column(db.String, primary_key = True)
    item = db.Column(db.String)
    total_wears = db.Column(db.Integer)
    cost_per_wear = db.Column(db.Integer)
    wears_per_month = db.Column(db.Integer)
    date_acquired = db.Column(db.String)
    cost = db.Column(db.Integer)
    source = db.Column(db.String)
    category = db.Column(db.String)

class WearCount(db.Model):
    __tablename__ = "wear_count"
    unique_id = db.Column(db.String, primary_key = True)
    month = db.Column(db.String)
    wears = db.Column(db.Integer)

######## API Routes ########
# This route renders the homepage



# This route returns info about individual items

    # DB query to table item_info
    # (ItemInfo is the class we defined above which references that table)

    # This query returns a sqlalchemy object that has to be parsed
    # Create an empty list to store our parsed object

    # Iterate through each object returned (which you can think of as a row from the table)

        # For each "row", create a dictionary from each column

        # Add each dictionary to the list

    # Return the list of dictionaries 



# IF WE HAVE TIME: This route returns wear counts by month for each item in the db

    # Same approach as above except that this time we are joining two tables
    # and pulling fields (columns) from both



######## Running the Flask App ########
# You need this - this allows you to actually run the app
if __name__ == "__main__":
    app.run(debug=True)