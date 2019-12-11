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
SELECT
  b.player_id,
  b.birthdate,
  b.nationality,
  b.firstname,
  b.lastname,
--   e.goals,
--   e.assists,
  st.tg as total_goals,
  st.ta as total_assists,
  st.tg + st.ta as total
FROM
  player_info b
--   INNER JOIN game_skater_stats e on (b.player_id = e.player_id)
  left join score_total st on (st.player_id = b.player_id)
WHERE EXTRACT(MONTH FROM birthdate)
BETWEEN 01 AND 12
;