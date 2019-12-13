select
	p.player_cnt,
	p.nationality,
	p.birthcity,
	w.city_ascii,
	w.iso3,
	w.lat,
	w.long
from worldcities as w
right join player_cnt as p on
p.birthcity=w.city_ascii and p.nationality=w.iso3;

