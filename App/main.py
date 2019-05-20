from App.player_info import PlayerInfo
import tkinter as tk
from PIL import ImageTk
import requests
from xml.etree import ElementTree

HEIGHT = 720
WIDTH = 1200

api_key = 'cvvxw2n26jggmr2py2z8mj26'


def display_recent_injuries(label):
    '''
    A method to display recent injuries on given label
    (tkinter.Label) -> None
    '''

    resp = requests.get(f"https://api.sportradar.us/nba/trial/v5/en/league/injuries.xml?api_key={api_key}")
    parent = ElementTree.fromstring(resp.content)
    child = list(parent)[0]
    text = ''

    for team in child:
        player = list(team)[0]
        injury = list(player)[0]
        text += player.get('full_name') + ' from ' + team.get('name') + ' was injured on ' + \
                injury.get('start_date') + ' with ' + injury.get('desc') + ' Updated on ' + \
                injury.get('update_date') + '.\n' + injury.get('comment') + '\n'

    label['text'] = text


def display_career_stats(player_name, label):
    '''
    A method to display given player career stats on given label
    (str, tkinter.Label) -> None
    '''

    player_info = PlayerInfo(player_name)

    if not player_info.id:
        label['text'] = 'Impossible to find ' + player_name

    else:
        career_stats = player_info.get_career_stats()
        text = ''

        for season in career_stats['rowSet']:
            text += f'In {season[1]} season {player_name} played for {season[4]} average {season[8]} minutes,' \
                f' scored {season[26]} points with {season[11]} FG% and {season[14]} FG3%. Also made {season[20]} ' \
                f'rebounds, {season[21]} assists, {season[22]} steals, {season[23]} blocks\n'

        label['text'] = text


def display_season_stats(player_name, year, label):
    '''
    A method to display given player's given season stats on given label
    (str, str, tkinter.Label) -> None
    '''

    player_info = PlayerInfo(player_name)

    if not player_info.id:
        label['text'] = f"Impossible to find {player_name}"

    else:
        try:
            season = player_info.get_year_stats(year)
            season = season[1]
            text = f'In {season[1]} season {player_name} played for {season[4]} average {season[8]} minutes,' \
                        f' scored {season[26]} points with {season[11]} FG% and {season[14]} FG3%.\nAlso made {season[20]} ' \
                        f'rebounds, {season[21]} assists, {season[22]} steals, {season[23]} blocks'

            label['text'] = text

        except:
            label['text'] = 'Wrong year data'


def display_player_injuries(player_name, label):
    '''
    A method to display given player's list of injuries on given label
    (str, tkinter.Label) -> None
    '''

    player_info = PlayerInfo(player_name)
    injuries = player_info.get_injuries()
    if not player_info.id:
        label['text'] = f"Impossible to find {player_name}"

    elif not injuries:
        label['text'] = f"{player_name} has not been injured"

    else:
        text = ''
        injuries = injuries[-31:-1]
        for injury in injuries:
            text += f'{injury[3]} was out on {injury[0]} in game for {injury[1]} with {injury[4]}.\n'

        label['text']  = text


def show_welcome_page():
    '''
    Hides current page and shows home page
    None -> None
    '''

    hide_all_elements()

    welcome_label = tk.Label(root, text="Welcome to NBA injuries! Choose one function below!")
    welcome_label.config(font=("Georgia", 30))
    welcome_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.1)
    elements.append(welcome_label)

    logo_image = ImageTk.PhotoImage(file='Pictures/logo.png')
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image
    logo_label.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.3)
    elements.append(logo_label)

    main_frame = tk.Frame(root, bd=1)
    main_frame.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)

    button1 = tk.Button(main_frame, text="Latest injuries", bg='gray', command=show_latest_injuries_page)
    button1.config(font=("Times New Roman", 18))
    button1.place(relwidth=0.5, relheight=0.5)
    elements.append(button1)

    button2 = tk.Button(main_frame, text="Find career stats", bg='gray', command=show_search_career_stats_page)
    button2.place(relx=0.5, relwidth=0.5, relheight=0.5)
    button2.config(font=("Times New Roman", 18))
    elements.append(button2)

    button3 = tk.Button(main_frame, text="Find season stats", bg='gray', command=show_season_stats_page)
    button3.place(relwidth=0.5, rely=0.5, relheight=0.5)
    button3.config(font=("Times New Roman", 18))
    elements.append(button3)

    button4 = tk.Button(main_frame, text="Find player injuries", bg='gray', command=show_search_injuries_page)
    button4.place(relx=0.5, relwidth=0.5, rely=0.5, relheight=0.5)
    button4.config(font=("Times New Roman", 18))
    elements.append(button4)
    elements.append(main_frame)


def show_search_career_stats_page():
    '''
    Hides current page and shows page for getting player's career stats
    None -> None
    '''

    hide_all_elements()

    search_frame = tk.Frame(root, bd=5)
    search_frame.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.15, anchor='n')

    search_label = tk.Label(search_frame, text="Enter a player name to find his career stats")
    search_label.config(font=('Times New Roman', 20))
    search_label.place(relx=0.5, relwidth=1, relheight=1/3, anchor='n')
    elements.append(search_label)

    search_entry = tk.Entry(search_frame)
    search_entry.config(font=('Times New Roman', 20))
    search_entry.place(rely=1/3, relwidth=0.65, relheight=2/3)
    elements.append(search_entry)

    search_button = tk.Button(search_frame, text="Search", command=lambda: display_career_stats(search_entry.get(),
                                                                                                info_label))
    search_button.config(font=('Times New Roman', 22))
    search_button.place(rely=1/3, relx=0.66, relheight=2/3, relwidth=0.34)
    elements.append(search_button)
    elements.append(search_frame)

    info_frame = tk.Frame(root, bd=10)
    info_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6, anchor='n')

    info_label = tk.Label(info_frame, justify='left')
    info_label.config(font=("Times New Roman", 13))
    info_label.place(relwidth=1, relheight=1)
    elements.append(info_label)
    elements.append(info_frame)

    menu_button = tk.Button(root, text="Menu", command=show_welcome_page)
    menu_button.config(font=('Times New Roman', 22))
    menu_button.place(relx=0.1, rely=0.87, relwidth=0.8, relheight=0.075)
    elements.append(menu_button)


def show_search_injuries_page():
    '''
    Hides current page and shows page for getting player's injuries list.
    None -> None
    '''

    hide_all_elements()

    search_frame = tk.Frame(root, bd=5)
    search_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.15, anchor='n')

    search_injuries_label = tk.Label(search_frame, text="Enter a player name to find his injuries")
    search_injuries_label.config(font=('Times New Roman', 20))
    search_injuries_label.place(relx=0.5, relwidth=1, relheight=1/3, anchor='n')
    elements.append(search_injuries_label)

    search_entry = tk.Entry(search_frame)
    search_entry.config(font=('Times New Roman', 20))
    search_entry.place(rely=1/3, relwidth=0.65, relheight=2/3)
    elements.append(search_entry)

    search_injuries_button = tk.Button(search_frame, text="Search", command=lambda: display_player_injuries(
        search_entry.get(), info_label))
    search_injuries_button.config(font=('Times New Roman', 22))
    search_injuries_button.place(rely=1/3, relx=0.66, relheight=2/3, relwidth=0.34)
    elements.append(search_injuries_button)
    elements.append(search_frame)

    info_frame = tk.Frame(root, bd=10)
    info_frame.place(relx=0.5, rely=0.22, relwidth=0.75, relheight=0.68, anchor='n')

    info_label = tk.Label(info_frame, justify='left')
    info_label.config(font=("Times New Roman", 13))
    info_label.place(relwidth=1, relheight=1)
    elements.append(info_label)
    elements.append(info_frame)

    menu_button = tk.Button(root, text="Menu", command=show_welcome_page)
    menu_button.config(font=('Times New Roman', 22))
    menu_button.place(relx=0.125, rely=0.92, relwidth=0.75, relheight=0.075)
    elements.append(menu_button)


def show_latest_injuries_page():
    '''
    Hides current page and shows page for getting last injuries
    None -> None
    '''

    hide_all_elements()

    latest_injuries_label = tk.Label(root, text="Here is described latest injuries")
    latest_injuries_label.config(font=("Times New Roman", 22))
    latest_injuries_label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)
    elements.append(latest_injuries_label)

    latest_injuries_frame = tk.Frame(root, bd=10)
    latest_injuries_frame.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.75)

    latest_injuries_info_label = tk.Label(latest_injuries_frame, justify='left')
    latest_injuries_info_label.config(font=("Times New Roman", 13))
    latest_injuries_info_label.place(relwidth=1, relheight=1)
    elements.append(latest_injuries_info_label)
    elements.append(latest_injuries_frame)

    menu_button = tk.Button(root, text="Menu", command=show_welcome_page)
    menu_button.config(font=('Times New Roman', 22))
    menu_button.place(relx=0.05, rely=0.9, relwidth=0.9, relheight=0.075)
    elements.append(menu_button)

    display_recent_injuries(latest_injuries_info_label)



def show_season_stats_page():
    '''
    Hides current page and shows page for getting player's season stats
    None -> None
    '''

    hide_all_elements()

    season_search_frame = tk.Frame(root, bd=5)
    season_search_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.2, anchor='n')

    season_search_player_label = tk.Label(season_search_frame, text="Enter a player name")
    season_search_player_label.config(font=('Times New Roman', 20))
    season_search_player_label.place(relwidth=0.2, relheight=1 / 6)
    elements.append(season_search_player_label)

    search_player_entry = tk.Entry(season_search_frame)
    search_player_entry.config(font=('Times New Roman', 20))
    search_player_entry.place(rely=1 / 6, relwidth=0.65, relheight=1 / 3)
    elements.append(search_player_entry)

    season_search_year_label = tk.Label(season_search_frame, text="Enter first year of season")
    season_search_year_label.config(font=('Times New Roman', 20))
    season_search_year_label.place(rely=0.5, relwidth=0.24, relheight=1 / 6)
    elements.append(season_search_year_label)

    search_year_entry = tk.Entry(season_search_frame)
    search_year_entry.config(font=('Times New Roman', 20))
    search_year_entry.place(rely=2 / 3, relwidth=0.65, relheight=1 / 3)
    elements.append(search_year_entry)

    season_search_button = tk.Button(season_search_frame, text="Search",
                                     command=lambda: display_season_stats(search_player_entry.get(),
                                                                          search_year_entry.get(), season_info_label))
    season_search_button.config(font=('Times New Roman', 20))
    season_search_button.place(relx=0.675, rely=1/6, relwidth=0.3, relheight= 5/6)
    elements.append(season_search_button)
    elements.append(season_search_frame)

    season_info_frame = tk.Frame(root, bd=5)
    season_info_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2, anchor='n')

    season_info_label = tk.Label(season_info_frame)
    season_info_label.config(font=("Times New Roman", 16))
    season_info_label.place(relwidth=1, relheight=1)
    elements.append(season_info_label)
    elements.append(season_info_frame)

    menu_button = tk.Button(root, text="Menu", command=show_welcome_page)
    menu_button.config(font=('Times New Roman', 22))
    menu_button.place(relx=0.125, rely=0.87, relwidth=0.75, relheight=0.075)
    elements.append(menu_button)


def set_background():
    '''
    Draws background picture
    None -> None
    '''

    background_image = ImageTk.PhotoImage(file='Pictures/background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)


def hide_all_elements():
    '''
    Hides all the elements, except background
    None -> None
    '''

    for element in elements:
        element.destroy()


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
    root = tk.Tk()
    root.title('NBA injuries')
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    elements = []

    set_background()

    show_welcome_page()
    root.mainloop()
