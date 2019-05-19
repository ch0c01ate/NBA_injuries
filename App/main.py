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
    # Damian Lillard had injuries only during 2017-18 season, so it is optimal to get his 2017-18 season stats for the
    # research

def process_user_input():
    '''
    A method to get user input and process it
    None -> None
    '''

    player_name = input("Enter player name: ")
    player_info = PlayerInfo(player_name)
    if player_info.id:
        for injury in player_info.get_injuries():
            print(' '.join(injury))

        career_stats = player_info.get_career_stats()

        headers = career_stats['headers']
        seasons = career_stats['rowSet']

        for season in seasons:
            for i in range(len(season)):
                print(headers[i], '-', season[i])

            print('')

    else:
        print("Wrong input data!")


if __name__ == '__main__':
    check_adt()
    process_user_input()