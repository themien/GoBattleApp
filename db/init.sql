CREATE DATABASE IF NOT EXISTS PoGoBattles;
USE PoGoBattles;

CREATE TABLE  IF NOT EXISTS Battle (
    battleId           INTEGER(8),
    season             INTEGER(4),
    league             VARCHAR(20),
    battleDate         DATE,
    battleTime         TIME,
    myPokemon1         VARCHAR(20),
    myPokemon2         VARCHAR(20),
    myPokemon3         VARCHAR(20),
    opponentName       VARCHAR(20),
    opponentPokemon1   VARCHAR(20),
    opponentPokemon2   VARCHAR(20),
    opponentPokemon3   VARCHAR(20),
    isWon              BOOLEAN,
    ifLostWasBadPlayed BOOLEAN,
    CONSTRAINT b_bid_pk PRIMARY KEY (battleId)
);

INSERT INTO Battle
  (battleId, season, league, battleDate, battleTime, 
   myPokemon1, myPokemon2, myPokemon3, opponentName,
   opponentPokemon1, opponentPokemon2, opponentPokemon3,
   isWon, ifLostWasBadPlayed
  )
VALUES
  (1, 7, 'Great', '2020-04-28', '14:34:55', 
   'Talonflame', 'Mew', 'Machamp (Shadow)', 'RandomOpp',
   'Azumarill', 'Altaria', 'Sableye', 
    True, NULL
  );


