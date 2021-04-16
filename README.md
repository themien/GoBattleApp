Welcome to GoBattleApp!

This App is a companion to the Pokemon Go "Go Battle League".

The purpose of this app is to store user battle data for analysing opponent teams and organising counters.

The information stored for each battle includes:
- Season: the current Go Battle League season
- League: the league type
- Elo: the trainer rank at the time of the battle
- Date: the battle date
- Time: the time when the battle took place
- My team: includes lead and the two backline Pokemons
- Opponent: Name and oposing team
- isWon: True if the battle was won

You will need docker-compose to build the app!

<code>
docker compose build</br>
docker compose up -d
</code>