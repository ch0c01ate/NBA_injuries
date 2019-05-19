from App.player_info import PlayerInfo

def check_adt():
    '''
    A method to demonstrate posibilities of adt
    None -> None
    '''

    player1 = PlayerInfo('Kyrie Irving')
    print(player1.get_injuries())
    print(player1.get_career_stats())
    print('')
    # Kyrie Irving had injuries during his entire career, so it is optimal to get his career stats for the research

    player2 = PlayerInfo('Damian Lillard')
    print(player2.get_injuries())
    print(player2.get_year_stats(2017))
    # Damian Lillard had injuries only during 2017-18 season, so it is optimal to get his 2017-18 season stats for the research

if __name__ == '__main__':
    check_adt()