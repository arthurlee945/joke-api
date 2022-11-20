from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
import os
import json

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SECRET_KEY"] = "biel31oib/23/-r_93lbfdu3ck39_dse3tn3i!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jokes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with open('./static/country_ISO.json', 'r') as file:
    country_info = json.load(file)


class Jokes(db.Model):
    __tablename__ = "jokes"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(250), nullable=False)
    joke = db.Column(db.String(1000), nullable=False)


with app.app_context():
    db.create_all()
    # def add_data():
    #     for c in country_info:
    #         try:
    #             with open(f"./json/{c}.json", 'r', encoding="utf8") as j_f:
    #                 data = json.load(j_f)
    #         except FileNotFoundError:
    #             no_jk = Jokes(
    #                 country=c,
    #                 joke="No Data Yet"
    #             )
    #             db.session.add(no_jk)
    #             db.session.commit()
    #         else:
    #             for jk in data[c]:
    #                 new_jk = Jokes(
    #                     country=c,
    #                     joke=jk
    #                 )
    #                 db.session.add(new_jk)
    #                 db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-jokes/<iso>")
def get_jokes(iso):
    if iso.upper() in country_info:
        jokes = [data.joke for data in db.session.query(Jokes).filter_by(country=iso.upper())]
        return jsonify(successful={
            iso.upper():jokes
        })
    else:
        flash("Log in before comments")
        return jsonify(error={
            "Wrong Country Code": "Please check https://countrycode.org/"
        })

if __name__ == "__main__":
    app.run(debug=True)

