
import os

import psycopg2

import numpy as np
import sqlalchemy
import pandas as pd


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
from collections import OrderedDict
from flask import Flask, jsonify, Response, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:Claymol1324@localhost:5432/Birthday_Effect')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres//postgres:Claymol1324@localhost:5432/Birthday_Effect"

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

db = SQLAlchemy(app)

# Save references to each table

game = Base.classes.game
player_info = Base.classes.player_info
# goalie = Base.classes.game_goalie_stats
# skater_info = Base.classes.game_skater_stats


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    
    return render_template("index.html")

############################
# USING ORM
##############################
@app.route("/players")
def sql_NHL_grabber():
    # Use Pandas to perform the sql query
    stmt = db.session.query(player_info).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.columns))
###########################################
# USING RAW SQL WITH PSYCOPG2
###########################################

@app.route("/bday_group1")
def group1():
    bdays = engine.execute('SELECT player_id, birthdate \
        FROM player_info \
        WHERE EXTRACT(MONTH FROM birthdate) \
        BETWEEN 01 AND 03;').fetchall()
    return jsonify(dict(bdays))

@app.route("/games_played")
def longevity():
    number_games = engine.execute(
    'SELECT player_id, COUNT(game_id) AS "games_played" \
        FROM game_skater_stats \
        GROUP BY player_id \
        ORDER BY games_played  \
        ;').fetchall()
    return dict(number_games)
if __name__ == '__main__':
    app.run(debug=True)

