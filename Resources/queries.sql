/*This keeps adding to the total count of a specified month range */
SELECT player_id, sum(count(player_id)) OVER (ORDER BY player_id)
FROM player_info
WHERE 
EXTRACT(MONTH FROM birthdate) 
BETWEEN 01 AND 03
GROUP BY player_id
;
/*This one just grabs the birthdates from specified month range */
SELECT birthdate FROM player_info
WHERE 
EXTRACT(MONTH FROM birthdate) 
BETWEEN 07 AND 09
;

/*counts goals for each player */
SELECT player_id, COUNT(goals) AS "goals" 
FROM game_skater_stats 
GROUP BY player_id 
ORDER BY goals DESC
LIMIT 100
;


with score_total as (
	select 
	  b.player_id,
	  sum(e.goals) as tg,
	  sum(e.assists) as ta
	from 
	  player_info b
	  inner join game_skater_stats e on (b.player_id = e.player_id)
	group by 
	  b.player_id
)

/* THis is the query that brings all of it */
with score_total as (
	select 
	  b.player_id,
	  sum(e.goals) as tg,
	  sum(e.assists) as ta,
	  count(e.game_id) as gm
	from 
	  player_info b
	  inner join game_skater_stats e on (b.player_id = e.player_id)
	group by 
	  b.player_id
)

SELECT
  b.player_id, 
  date_part('month', b.birthdate) as birthmonth,
  b.nationality,
  b.firstname,
  b.lastname,

  st.tg as total_goals,
  st.ta as total_assists,
  st.tg + st.ta as points,
  st.gm as total_games
FROM
  player_info b
  left join score_total st on (st.player_id = b.player_id)
  WHERE gm > 20
ORDER BY birthmonth
;

/************************
//this one returns all the birthmonths ascending and total points they had
*/
with score_total as (
	select 
	  b.player_id,
	  sum(e.goals) as tg 
	from 
	  player_info b
	  inner join game_skater_stats e on (b.player_id = e.player_id)
	group by 
	  b.player_id
)
SELECT
  date_part('month', b.birthdate) as birthmonth, 
  st.tg as total_goals
FROM
  player_info b
  left join score_total st on (st.player_id = b.player_id)
ORDER BY birthmonth
;
