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




