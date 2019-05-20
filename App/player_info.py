from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import csv
import json

class PlayerInfo:
    """
    A class to get different NBA player's information
    """

    def __init__(self, name):
        """Initial function for the class

            Args:
                self: self
                name (str): Player name to work with
        """

        self.player_name = name
        self.id = self.find_player_id()

    def find_player_id(self):
        """A method to find player's id

            Args:
                self: self

            Returns:
                if (int): player's id, found in nba_api
        """
        for player in players.get_players():
            if player['full_name'].lower() == self.player_name.lower():
                return player['id']

    def get_injuries(self):
        """A method to find all player's injuries

            Args:
                self: self

            Returns:
                injuries(list): List of injuries, got from csv file
        """

        injuries = []

        if not self.id:
            return injuries

        with open('data/injuries.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if self.player_name.lower() in row[3].lower():
                    injuries.append(row)

        return injuries

    def get_career_stats(self):
        """A method to get player's career stats

            Args:
                self: self

            Returns:
                career_stats(dict): Dictionary with list of season stats and headers
        """

        if not self.id:
            return {}
        return json.loads(playercareerstats.PlayerCareerStats(player_id=self.id).get_json())['resultSets'][0]

    def get_year_stats(self, year):
        """A method to get player's career stats

            Args:
                self: self
                year(int or str): year, when the season begins

            Returns:
                tuple: Tuple with headers and asked season
        """

        if not self.id:
            return ()
        career_stats = self.get_career_stats()
        for season in career_stats['rowSet']:
            if str(year) in season[1]:
                return (career_stats['headers'], season)
