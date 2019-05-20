from App.player_info import PlayerInfo

class PlayerInfoTest:
    """
    A class with collection of unit tests for PlayerInfo
    """

    def test_with_usual_data(self):
        """
        A method that tests PlayerInfo with existed data
        """

        player = PlayerInfo('Lebron James')
        assert player.id == 2544, 'Wrong player id'
        assert type(player.get_injuries()) == list, 'Injuries Should be in a list'
        assert player.get_injuries() != [], "List of Lebron James' injuries is not empty"
        assert type(player.get_career_stats()) == dict, 'Career stats should be a dict'
        assert type(player.get_year_stats(2015)) == tuple, 'Year stats should be a tuple'

    def test_with_wrong_data(self):
        """
        A method that tests PlayerInfo with wrong data
        """

        player = PlayerInfo('Duwayane Wade')
        assert player.id == None, 'Id of wrong player should be None'
        assert player.get_injuries() == [], "List of wrong player's injuries should be empty"
        assert player.get_career_stats() == {}, 'Career stats of wrong player should be an empty dict'
        assert player.get_year_stats(2015) == (), 'Year stats of wrong player should be an empty tuple'

    def test_with_empty_data(self):
        """
        A method that tests PlayerInfo with empty data
        (self) -> None
        """

        player = PlayerInfo('')
        assert player.id == None, 'Id of empty player should be None'
        assert player.get_injuries() == [], "List of empty player's injuries should be empty"
        assert player.get_career_stats() == {}, 'Career stats of empty player should be an empty dict'
        assert player.get_year_stats(2015) == (), 'Year stats of empty player should be an empty tuple'


if __name__ == '__main__':
    test = PlayerInfoTest()
    test.test_with_empty_data()
    test.test_with_usual_data()
    test.test_with_wrong_data()
    print("Passed!")