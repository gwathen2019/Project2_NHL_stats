
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
    
    return render_template("index_NHL.html")

@app.route("/bday_group1")

def group1():
    bdays = engine.execute('\
with score_total as (\
	select\
	  b.player_id,\
	  sum(e.goals) as tg,\
	  sum(e.assists) as ta,\
      count(e.game_id) as gm\
	 from\
	  player_info b\
	  inner join game_skater_stats e on (b.player_id = e.player_id)\
	group by\
	  b.player_id\
)\
SELECT\
  b.player_id, \
  b.birthdate, \
  b.nationality,\
  b.firstname,\
  b.lastname,\
  st.tg as total_goals,\
  st.ta as total_assists,\
  st.tg + st.ta as points,\
  st.gm as total_games\
 FROM\
  player_info b\
  left join score_total st on (st.player_id = b.player_id)\
 WHERE EXTRACT(MONTH FROM birthdate)\
 BETWEEN 01 AND 03\
 ORDER BY points DESC\
 ;\
    ').fetchall()
    
    group_1 = {}
    
    for each in bdays:
        group_1[each[0]] = each[:]
     
    return jsonify(group_1)

@app.route("/games_played")
def longevity():

    number_games = engine.execute(
    'SELECT player_id, COUNT(game_id) AS "games_played" \
        FROM game_skater_stats \
        GROUP BY player_id \
        ORDER BY games_played  \
        ;').fetchall()
    
    games_played = {}
    
    for each in number_games:
        games_played[each[0]] = each[1]

    return jsonify(games_played)

@app.route("/USA")
def manualUSA():

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [280,270,230,285,225,180,140,175,145,80,130,145],
        "type": "scatter"
    }

    return jsonify(plot_trace)   

@app.route("/CAN")
def manualCAN():

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [212,170,330,485,625,120,110,105,125,90,160,115],
        "type": "scatter"
    }

    return jsonify(plot_trace)

@app.route("/CHE")
def manualCHE():

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [145,180,230,785,125,220,110,85,95,90,80,45],
        "type": "scatter"
    }

    return jsonify(plot_trace)

if __name__ == '__main__':
    app.run(debug=True)

