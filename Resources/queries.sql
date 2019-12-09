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