import numpy as np
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from collections import OrderedDict
from flask import Flask, jsonify, Response, render_template
import psycopg2
import json


#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:postgres@localhost:5432/NHL Stats')

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
    bdays = engine.execute("\
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
  date_part('month', birthdate) as birthmonth, \
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
  WHERE gm > 20 \
  ORDER BY birthmonth\
 ;\
    ").fetchall()
    
    plyrid = []
    bmonth= []
    nation= []
    first=[]
    last=[]
    tl_goals=[]
    tl_assists=[]
    tl_points=[]
    tl_games=[]

    for x in bdays:
        pl_id = x[0]
        month_born = x[1]
        nationality = x[2]
        firstname = x[3]
        lastname = x[4]
        goals = x[5]
        assists=x[6]
        points=x[7]
        games=x[8]
        plyrid.append(pl_id)
        bmonth.append(month_born)
        nation.append(nationality)
        first.append(firstname)
        last.append(lastname)
        tl_goals.append(goals)
        tl_assists.append(assists)
        tl_points.append(points)
        tl_games.append(games)

    data = {
        "id" : plyrid,
        "birth_month" : bmonth,
        "nation" : nationality,
        "first_name": first,
        "last_name": last,
        "goals" : tl_goals,
        "assists" : tl_assists,
        "points" : tl_points,
        "games" : tl_games
    }
    

    return jsonify(data)
     
    # return jsonify(big_fat_dict)

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

@app.route("/goals")
def scoring():

    goals = engine.execute("\
    with score_total as (\
	select \
	  b.player_id,\
	  sum(e.goals) as tg,\
      count(e.game_id) as gm \
	from \
	  player_info b\
	  inner join game_skater_stats e on (b.player_id = e.player_id)\
	group by \
	  b.player_id\
    )\
    SELECT\
    date_part('month', b.birthdate) as birthmonth, \
    st.tg as total_goals,\
    st.gm as total_games\
    FROM\
    player_info b\
    left join score_total st on (st.player_id = b.player_id)\
    WHERE gm > 20\
    ORDER BY birthmonth\
    ;" ).fetchall()
    
    gls = []
    gls2 = []
    
    for x in goals:
        key = x[0]
        value = x[1]
        gls.append(key)
        gls2.append(value)
    
    goals = {
        "birthmonth":gls,
        "goals":gls2
    }
   
    return jsonify(goals)

@app.route("/USA")
def manualUSA():

    bdays = engine.execute("\
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
    date_part('month', birthdate) as birthmonth, \
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
    WHERE gm > 20 \
    AND b.nationality = 'USA'\
    ORDER BY birthmonth\
    ;\
        ").fetchall()
        
    months = []
    for x in bdays:
                month_born = x[1]
                months.append(month_born)

    Jan = len([i for i in months if 0 < i < 2])
    Feb = len([i for i in months if 1 < i < 3])
    Mar = len([i for i in months if 2 < i < 4])
    Apr = len([i for i in months if 3 < i < 5])
    May = len([i for i in months if 4 < i < 6])
    June = len([i for i in months if 5 < i < 7])
    July = len([i for i in months if 6 < i < 8])
    Aug = len([i for i in months if 7 < i < 9])
    Sept = len([i for i in months if 8 < i < 10])
    Oct = len([i for i in months if 9 < i <11])
    Nov = len([i for i in months if 10< i < 12])
    Dec = len([i for i in months if 11 < i < 13])
    
    plot_trace = {
        "x": ["January","February","March","April","May","June","July","August","September","October","November","December"],
        "y": [Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec],
        "type": "scatter"
    }

    return jsonify(plot_trace)   

@app.route("/CAN")
def manualCAN():

    bdays = engine.execute("\
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
    date_part('month', birthdate) as birthmonth, \
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
    WHERE gm > 20 \
    AND b.nationality = 'CAN'\
    ORDER BY birthmonth\
    ;\
        ").fetchall()
        
    
    months = []
    for x in bdays:
                month_born = x[1]
                months.append(month_born)

    Jan = len([i for i in months if 0 < i < 2])
    Feb = len([i for i in months if 1 < i < 3])
    Mar = len([i for i in months if 2 < i < 4])
    Apr = len([i for i in months if 3 < i < 5])
    May = len([i for i in months if 4 < i < 6])
    June = len([i for i in months if 5 < i < 7])
    July = len([i for i in months if 6 < i < 8])
    Aug = len([i for i in months if 7 < i < 9])
    Sept = len([i for i in months if 8 < i < 10])
    Oct = len([i for i in months if 9 < i <11])
    Nov = len([i for i in months if 10< i < 12])
    Dec = len([i for i in months if 11 < i < 13])
    



    plot_trace = {
        "x": ["Januar","February","March","April","May","June","July","August","September","October","November","December"],
        "y": [Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec],
        "type": "scatter"
    }

    return jsonify(plot_trace)

@app.route("/CHE")
def manualFIN():
    
    bdays = engine.execute("\
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
    date_part('month', birthdate) as birthmonth, \
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
    WHERE gm > 20 \
    AND b.nationality = 'FIN' OR b.nationality = 'CHE' OR b.nationality = 'SWE' OR b.nationality = 'RUS' OR b.nationality = 'SVK' OR b.nationality = 'DEU'\
    OR b.nationality = 'CZE' OR b.nationality = 'SVN'\
    ORDER BY birthmonth\
    ;\
        ").fetchall()
        
    
    months = []
    for x in bdays:
                month_born = x[1]
                months.append(month_born)

    Jan = len([i for i in months if 0 < i < 2])
    Feb = len([i for i in months if 1 < i < 3])
    Mar = len([i for i in months if 2 < i < 4])
    Apr = len([i for i in months if 3 < i < 5])
    May = len([i for i in months if 4 < i < 6])
    June = len([i for i in months if 5 < i < 7])
    July = len([i for i in months if 6 < i < 8])
    Aug = len([i for i in months if 7 < i < 9])
    Sept = len([i for i in months if 8 < i < 10])
    Oct = len([i for i in months if 9 < i <11])
    Nov = len([i for i in months if 10< i < 12])
    Dec = len([i for i in months if 11 < i < 13])
    



    plot_trace = {
        "x": ["January","February","March","April","May","June","July","August","September","October","November","December"],
        "y": [Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec],
        "type": "scatter"
    }

    return jsonify(plot_trace)

@app.route("/table")
def player_table():
    players_table_query = """SELECT 
            b.player_id,
            b.lastName,
            b.firstName,
            b.nationality,
            b.birthCity,
            b.birthDate,
            SUM(e.goals) AS total_goals,
            SUM(e.assists) AS total_assists,
            COUNT(e.game_id) AS games_played
        FROM 
	        player_info b
	    INNER JOIN game_skater_stats e ON (b.player_id = e.player_id)
        GROUP BY
	    b.player_id;"""
    sel = engine.execute(players_table_query).fetchall()
    # need to make into a dictionary, then use js to make table!
    #def Convert(sel): 
    #res_dct = {sel[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    #return res_dct 


    print("df is here")
    return jsonify(df)

if __name__ == '__main__':
    app.run(debug=True)

