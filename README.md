PL:

API DOCS:  https://www.balldontlie.io/

Skrypt umożliwia wyświetlanie róznego zestawu danych o tematyce NBA według wpisania odpowiednich parametrów w konsoli


Wyświetlanie pogrupowanych zespołów według dywyzji:

python <nazwa_skryptu.py> grouped-teams
Ex:

Southeast
    Atlanta Hawks (ATL)
    Charlotte Hornets (CHA)
    <reszta zespolow>
Atlantic
    Boston Celtics (BOS)
    <reszta zespolow>



Wyświetlanie najcięższego oraz najwyższego zawodnika według podanego imienia lub nazwiska:
--name parameter

python <nazwa_skryptu.py> players-stats --name <imie_zawodnika lub nazwisko_zawodnika>
        
Ex:
        
python API_connect.py players-stats --name Harden

The tallest player: James Harden 1.96 meters
The heaviest player:  James Harden 99 kilograms
        
python API_connect.py players-stats --name Josh
        
The tallest player: Josh Jackson 2.03 meters
The heaviest player:  Josh Hart 97 kilograms


Wyświetlanie statystyk zespołów za dany sezon oraz opcjonalne zapisanie je w pliku
--season parameter
--output parameter

csv - zapisywanie danych jako csv

json - zapisywanie danych jako json

sqlite - zapisywanie danych do sqlite database

stdout - wyswietlanie standardowego wyjscia do konsoli (bez zapiswania wynikow)
      
Przykładowy json dla parametorw season = 2018 
        
python <nazwa_skryptu.py> teams-stats --season 2018 --output json
        
{
    "Denver Nuggets": [
        "won games as home team: 3",
        "won games as visitor team: 1",
        "lost games as home team: 0",
        "lost games as visitor team: 2"
    ],
    "Minnesota Timberwolves": [
        "won games as home team: 2",
        "won games as visitor team: 0",
        "lost games as home team: 1",
        "lost games as visitor team: 3"
    ],
      <reszta_zespolow>
}  

        
        
        
        
ENG:
             
          
API DOCS: https://www.balldontlie.io/

This script allows you to display a different set of NBA data by entering the appropriate parameters in the console


Display grouped teams by division:

python <script_name.py> grouped-teams
Ex:

Southeast
    Atlanta Hawks (ATL)
    Charlotte Hornets (CHA)
    <rest of the teams>
Atlantic
    Boston Celtics (BOS)
    <other teams>.



Display the heaviest and tallest players by given name or surname:
--name parameter

python <script_name.py> players-stats --name <player_name or player_name>
        
Ex:
        
python API_connect.py players-stats --name Harden

The tallest player: James Harden 1.96 meters
The heaviest player: James Harden 99 kilograms
        
python API_connect.py players-stats --name Josh
        
The tallest player: Josh Jackson 2.03 meters
The heaviest player: Josh Hart 97 kilograms


Displaying the team statistics for a given season and optionally saving them in a file
--season parameter
--output parameter

csv - save data as csv

json - save data as json

sqlite - write data to sqlite database

stdout - display standard output to the console (without saving the results)
      
Example json for parameters season = 2018 
        
python <script_name.py> teams-stats --season 2018 --output json
        
{
    "Denver Nuggets": [
        "won games as home team: 3",
        "won games as visitor team: 1",
        "lost games as home team: 0",
        "lost games as visitor team: 2"
    ],
    "Minnesota Timberwolves": [
        "won games as home team: 2",
        "won games as visitor team: 0",
        "lost games as home team: 1",
        "lost games as visitor team: 3"
    ],
      <other_teams>.
}  


          





