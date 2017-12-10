

CREATE TABLE games (
  `game_id` char(36) NOT NULL,
  `first_code_peg` TINYINT NOT NULL,
  `second_code_peg` TINYINT NOT NULL,
  `third_code_peg` TINYINT NOT NULL,
  `fourth_code_peg` TINYINT NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

