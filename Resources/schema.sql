
CREATE TABLE player_info (
  player_id INT PRIMARY KEY,
  firstName character varying(45) ,
  lastName character varying(45) ,
  nationality character varying(45) ,
  birthCity character varying(45) ,
  primaryPostion character varying(10) ,
  birthDate DATE NOT NULL,	
  link character varying(145) 
);

CREATE TABLE game (
  game_id INT PRIMARY KEY,
  season INT,
  type character varying (45),
  date_time DATE ,
  away_team_id INT ,
  home_team_id INT ,
  away_goals INT ,
  home_goals INT ,
  outcome character varying (45),
  home_rink_side_start character varying (45),
  venue character varying (45),
  venue_link character varying (155),
  venue_time_zone_id character varying (155),
  venue_time_zone_offset character varying (155) ,
  venue_time_zone_tz character varying (6)
);

CREATE TABLE game_skater_stats (
  game_id INT ,
  player_id INT ,
  team_id INT ,
  timeOnice INT ,
  assists INT ,
  goals INT ,
  shots INT ,
  hits INT ,
  powerPlayGoals INT ,
  powerPlayAssists INT ,
  penaltyMinutes INT ,
  faceOffWins INT ,
  face0ffTaken INT ,
  takeaways INT ,
  giveaways INT ,
  shortHandedGoals INT ,
  shortHandedAssists INT ,
  blocked INT ,
  plusMinus INT ,
  evenTimeOnIce INT ,
  shortHandedTimeOnIce INT ,
  powerPlayTimeOnIce INT ,
  FOREIGN KEY (player_id) REFERENCES player_info(player_id),
  FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE game_goalie_stats (
  game_id INT ,
  player_id INT ,
  team_id INT ,
  timeOnIce INT ,
  assists INT ,
  goals INT ,
  pim INT ,
  shots INT ,
  saves INT ,
  powerPlaySaves INT ,
  shortHandedSaves INT ,
  evenSaves INT ,
  shortHandedShotsAgainst INT ,
  evenShotsAgainst  INT ,
  powerPlaySHotsAgainst INT ,
  decision character varying (45) ,
  savePercentage character varying (45) ,
  powerPlaySavePercentage character varying (155) ,
  evenStrengthSavePercentage character varying (155) ,
  FOREIGN KEY (player_id) REFERENCES player_info(player_id),
  FOREIGN KEY (game_id) REFERENCES game(game_id)
);

