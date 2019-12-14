
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
engine = create_engine('postgres+psycopg2://postgres:Ursus2000@localhost:5432/Project2_NHL_Stats')

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
#     USA = engine.execute("\
#       with score_total as (\
# 	select\
# 	  b.player_id,\
# 	  sum(e.goals) as tg,\
# 	  sum(e.assists) as ta,\
#       count(e.game_id) as gm\
# 	 from\
# 	  player_info b\
# 	  inner join game_skater_stats e on (b.player_id = e.player_id)\
# 	group by\
# 	  b.player_id\
#     )\
#     SELECT\
#   b.player_id, \
#   b.birthdate, \
#   b.nationality,\
#   b.firstname,\
#   b.lastname,\
#   st.tg as total_goals,\
#   st.ta as total_assists,\
#   st.tg + st.ta as points,\
#   st.gm as total_games\
#  FROM\
#   player_info b\
#   left join score_total st on (st.player_id = b.player_id)\
#   WHERE nationality = 'USA'\
#  ORDER BY points DESC\
#  ;\
#     ").fetchall()
#     Jan1 = {}

#     for each in USA:
#         Jan1[each[1]] = each[1]
    
    
#     Jan_bday = {}
#     for each in Jan1:
#         Jan_bday[each[2]] = each[2]
    
#     for row in Jan1:
#         d = dict(row.items())
#         d['Tags'] = d['Keywords']

#     return jsonify(str(d))

    Jan = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND \
        EXTRACT\
        (MONTH FROM birthdate)\
	    BETWEEN 01 AND 01 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uJan = len(Jan)

    Feb = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 02 AND 02 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uFeb = len(Feb)

    Mar = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND \
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 03 AND 03 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uMar = len(Mar)


    Apr = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate) \
	    BETWEEN 04 AND 04 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uApr = len(Apr)

    May = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 05 AND 05 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uMay = len(May)

    June = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 06 AND 06 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uJune = len(June)

    July = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 07 AND 07 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uJuly = len(July)

    Aug = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 08 AND 08 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uAug = len(Aug)

    Sept = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 09 AND 09 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uSept = len(Sept)

    Oct = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 10 AND 10 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uOct = len(Oct)

    Nov = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 11 AND 11 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uNov = len(Nov)

    Dec = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'USA' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 12 AND 12 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uDec = len(Dec)

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [uJan, uFeb, uMar, uApr, uMay, uJune, uJuly, uAug, uSept, uOct, uNov, uDec],
        "type": "scatter"
    }

    return jsonify(plot_trace)   

@app.route("/CAN")
def manualCAN():

    Jan = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND \
        EXTRACT\
        (MONTH FROM birthdate)\
	    BETWEEN 01 AND 01 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uJan = len(Jan)

    Feb = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 02 AND 02 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uFeb = len(Feb)

    Mar = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND \
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 03 AND 03 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uMar = len(Mar)


    Apr = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate) \
	    BETWEEN 04 AND 04 \
        GROUP BY birthdate \
        ;").fetchall()
    
    uApr = len(Apr)

    May = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 05 AND 05 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uMay = len(May)

    June = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 06 AND 06 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uJune = len(June)

    July = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 07 AND 07 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uJuly = len(July)

    Aug = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 08 AND 08 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uAug = len(Aug)

    Sept = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 09 AND 09 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uSept = len(Sept)

    Oct = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 10 AND 10 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uOct = len(Oct)

    Nov = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 11 AND 11 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uNov = len(Nov)

    Dec = engine.execute("SELECT COUNT(birthdate) \
        FROM player_info\
        WHERE nationality = 'CAN' AND\
        EXTRACT(MONTH FROM birthdate)\
	    BETWEEN 12 AND 12 \
        GROUP BY birthdate \
        ORDER BY birthdate DESC\
        ;").fetchall()
    
    uDec = len(Dec)

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [uJan, uFeb, uMar, uApr, uMay, uJune, uJuly, uAug, uSept, uOct, uNov, uDec],
        "type": "scatter"
    }

    return jsonify(plot_trace)

@app.route("/FIN")
def manualFIN():
    
    Jan = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 01 AND 01\
    ;").fetchall() 
    
    uJan = len(Jan)

    Feb = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 02 AND 02\
    ;").fetchall()
    
    uFeb = len(Feb)

    Mar = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 03 AND 03\
    ;").fetchall()
    
    uMar = len(Mar)


    Apr = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 04 AND 04\
    ;").fetchall()
    
    uApr = len(Apr)

    May = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 05 AND 05\
    ;").fetchall()
    
    uMay = len(May)

    June = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 06 AND 06\
    ;").fetchall()
    
    uJune = len(June)

    July = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 07 AND 07\
    ;").fetchall()
    
    uJuly = len(July)

    Aug = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 08 AND 08\
    ;").fetchall()
    
    uAug = len(Aug)

    Sept = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 09 AND 09\
    ;").fetchall()
    
    uSept = len(Sept)

    Oct = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 10 AND 10\
    ;").fetchall()
   
    uOct = len(Oct)

    Nov = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 11 AND 11\
    ;").fetchall()
    
    uNov = len(Nov)

    Dec = engine.execute("SELECT birthdate, firstname, lastname, nationality FROM player_info\
    WHERE \
	(\
	nationality = 'FIN' OR nationality = 'CHE' OR nationality = 'SWE' OR nationality = 'RUS' OR nationality = 'SVK'OR nationality = 'DEU'\
    OR nationality = 'CZE'OR nationality = 'SVK' OR nationality = 'SVN')\
    AND \
	EXTRACT(MONTH FROM birthdate)\
	BETWEEN 12 AND 12\
    ;").fetchall()
    
    uDec = len(Dec)

    plot_trace = {
        "x": ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"],
        "y": [uJan, uFeb, uMar, uApr, uMay, uJune, uJuly, uAug, uSept, uOct, uNov, uDec],
        "type": "scatter"
    }

    return jsonify(plot_trace)


if __name__ == '__main__':
    app.run(debug=True)

