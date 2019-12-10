
import numpy as np
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from collections import OrderedDict
from flask import Flask, jsonify, Response, render_template
import psycopg2

#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:Claymol1324@localhost:5432/Birthday_Effect')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    
    return render_template("index.html")

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

    # group1 = {
    #     "games" : number_games,
    #     "bdays" : bdays
    # }
    
    


if __name__ == '__main__':
    app.run(debug=True)

