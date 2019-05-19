from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import csv
import json

class PlayerInfo:
    '''
    A class to get different NBA player's information
    '''

    def __init__(self, name):
        '''
        An initial method
        (self, str) -> None
        '''
        self.player_name = name
        self.id = self.find_player_id()

    def find_player_id(self):
        '''
        A method to find player id by name
        (self) -> int
        '''
        for player in players.get_players():
            if player['full_name'].lower() == self.player_name.lower():
                return player['id']

    def get_injuries(self):
        '''
        A method to find all player's injuries
        (self) -> list
        '''
        injuries = []
        with open('data/injuries.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if self.player_name.lower() in row[3].lower():
                    injuries.append(row)

        return injuries

    def get_career_stats(self):
        '''
        A method to find player's career statistics
        (self) -> dict
        '''
        return json.loads(playercareerstats.PlayerCareerStats(player_id=self.id).get_json())['resultSets'][0]

    def get_year_stats(self, year):
        '''
        A method to find player's statistics for given season
        (self) -> tuple
        '''
        career_stats = self.get_career_stats()
        for season in career_stats['rowSet']:
            if str(year) in season[1]:
                return (career_stats['headers'], season)




