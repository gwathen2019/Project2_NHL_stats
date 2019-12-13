select
	p.nationality, p.birthcity, count(p.player_id) as player_cnt
	from player_info as p
	group by p.nationality, p.birthcity
	order by player_cnt desc;