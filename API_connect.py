from urllib import response
import requests
import sys
import csv
import sqlite3
import json



class ApiConnect:
    def __init__(self,response:str) -> None:
        self.response = response


    def sql_output(self,divisions):
        connection = sqlite3.connect("nba.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS nba (won_games_as_home_team text,won_games_as_visitor_team text,lost_games_as_home_team text,lost_games_as_visitor_team text)")
        cursor.executemany("INSERT INTO nba VALUES (?,?,?,?)",divisions.values()) 
        connection.commit()
        cursor.execute("SELECT * FROM nba")
        print(cursor.fetchall())
        connection.execute("DROP TABLE nba")
        connection.close()


    def csv_output(self,teams_dic): ## wyjscie do pliku CSV
        with open("nba.csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in teams_dic.items():
                writer.writerow([key, ','.join(value)])
               
    

    def json_output(self,teams_dic): ## wyjscie do pliku JSON
        with open("nba.json","w") as json_file:
            json.dump(teams_dic,json_file,indent=4)
            

    def std_out(self,teams): ## wyjscie do konsoli
        for key,values in teams.items():
            print(key)
            for v in values:
                print(v)

    
    def show_grouped_teams(self): ## Wyswietlanie zespolow wedlug dywyzji

        divisions = ("Northwest","Southwest","Pacific","Atlantic","Central","Southeast") ## Tuple z nazwami dywyzji
        for div in divisions:
            print(div)
            for teams in self.response.json()['data']:
                if teams['division'] == div:
                    print(f"    {teams['full_name']} ({teams['abbreviation']})")## wyswietlanie nazwy zespou i abbrew
        
      

    def show_players_stats(self):       ## zwraca najciezszego i najwyzszego wedlug jego first name 
        lista_wzrostu = [] #lista wzrostu z ktorego bedzie wybierany najwiekszy element
        lista_wag = [] #lista wag z ktorego bedzie wybierany najwiekszy element
        dic = {}
        for players in self.response.json()['data']:
                if players["height_inches"] != None: ## wykluczenie zawodnikow z None w danych
                    dic[players["first_name"] + " " + players["last_name"]] = [(players['height_feet']*30.48)+(players['height_inches']*2.54),round(players['weight_pounds']*0.45,2)] ## tworzenie slownika
        # z lista zawierajaca wzrost oraz wage, gdzie key to imie i nazwisko zawodnika a value to lista zawierajaca wzrost i wage

        for values in dic.values():
            lista_wzrostu.append(values[0]) ## Tworzenie listy z pierwszych elementow listy w slowniku
            lista_wag.append(values[1]) ## -|- z drugich elementow w slowniku
        try:
            max_height = max(lista_wzrostu) 
            max_weight = max(lista_wag)
        except ValueError:
            print(f"Nie ma zawodnika o imieniu lub nazwisku {sys.argv[3]}")
            print(f"The tallest player: Not found \nThe heaviest player: Not found")

        
        for x in dic: ## wyswietlanie zawodnikow w konsoli
            if max_height in dic[x]: ## jesli dany zawodnik posiada w values wzrost max_height -> zwroc imie i nazwisko zawodnika
                print(f"The tallest player: {x} {round(max_height)*0.01} meters")
            if max_weight in dic[x]:
                print(f"The heaviest player:  {x} {max_weight} kilograms")
            




    def show_teams_stats(self):
        teams = {'Denver Nuggets':[], 'Minnesota Timberwolves':[], 'Oklahoma City Thunder':[], 'Portland Trail Blazers':[], 'Utah Jazz':[], 
        'Dallas Mavericks':[], 'Houston Rockets':[], 'Memphis Grizzlies':[], 'New Orleans Pelicans':[], 'San Antonio Spurs':[],
        'Golden State Warriors':[], 'LA Clippers':[], 'Los Angeles Lakers':[], 'Phoenix Suns':[], 'Sacramento Kings':[],
        'Boston Celtics':[], 'Brooklyn Nets':[], 'New York Knicks':[], 'Philadelphia 76ers':[], 'Toronto Raptors':[], 'Chicago Bulls':[],
        'Cleveland Cavaliers':[], 'Detroit Pistons':[], 'Indiana Pacers':[], 'Milwaukee Bucks':[],
        'Atlanta Hawks':[], 'Charlotte Hornets':[], 'Miami Heat':[], 'Orlando Magic':[], 'Washington Wizards':[]}

    
        for team in teams: ## wyswitlanie wynikow zespolow wedlug poszczegolnych sezonow 
            Won_games_as_home_team = 0
            Won_games_as_visitor_team = 0
            Lost_games_as_home_team = 0
            Lost_games_as_visitor_team = 0
            for games in self.response.json()['data']:
                if games['home_team']['full_name'] == team: 
                    if games['home_team_score'] > games['visitor_team_score']:
                        Won_games_as_home_team = Won_games_as_home_team + 1
                    else:
                        Lost_games_as_home_team = Lost_games_as_home_team + 1
                
                
                if games['visitor_team']['full_name'] == team:
                    if games['home_team_score'] < games['visitor_team_score']:
                        Won_games_as_visitor_team = Won_games_as_visitor_team + 1
                    else:
                        Lost_games_as_visitor_team = Lost_games_as_visitor_team + 1
                
            teams[team] = [f"won games as home team: {Won_games_as_home_team}",f"won games as visitor team: {Won_games_as_visitor_team}"
            ,f"lost games as home team: {Lost_games_as_home_team}",f"lost games as visitor team: {Lost_games_as_visitor_team}"]

        
        
        ############### Wyswietlanie wyniku wedlug podanego parametru
        
    
        if sys.argv[5] == "sqlite":
            self.sql_output(teams) 
        elif sys.argv[5] == "csv":
            self.csv_output(teams)
        elif sys.argv[5] == "json":
            self.json_output(teams)
        elif sys.argv[5] == "stdout":
            self.std_out(teams)
        else:
            print("Nie prawidlowe dane wejsciowe")
            

##############################################################
                

if len(sys.argv) < 2:
    print("Nie podano argumentow")
    exit(0)
else:
    try:
        if sys.argv[1] == "grouped-teams":
            response = requests.get(f'https://www.balldontlie.io/api/v1/teams/')
            if response.status_code == 200:
                api = ApiConnect(response)
                api.show_grouped_teams()

        elif sys.argv[1] == "players-stats" and sys.argv[2] == "--name": #Not all players will have height_feet, height_inches, or weight_pounds.
            response = requests.get(f'https://www.balldontlie.io/api/v1/players?search={sys.argv[3]}&per_page=100')
            if response.status_code == 200:
                api = ApiConnect(response)
                api.show_players_stats()


        elif sys.argv[1] == "teams-stats" and sys.argv[2] == "--season": ## wy??wietlanie statystyk zespolow wedlug podanego sezonu 
            response = requests.get(f'https://www.balldontlie.io/api/v1/games?seasons[]={sys.argv[3]}&per_page=100&page=1')
            if response.status_code == 200:
                api = ApiConnect(response)
                api.show_teams_stats()
        
            
    except IndexError:
        print("Bledne dane wejsciowe")
        exit(0)



