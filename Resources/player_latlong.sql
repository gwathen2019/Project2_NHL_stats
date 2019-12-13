select * from player_info;
select * from worldcities;
-- Perform an INNER JOIN on the two tables
SELECT p.player_id, p.firstname, p.lastname, p.nationality, p.birthcity, w.city_ascii, w.iso3, w.lat, w.long
FROM worldcities as w
INNER JOIN player_info AS p ON
p.birthcity=w.city_ascii and p.nationality=w.iso3;