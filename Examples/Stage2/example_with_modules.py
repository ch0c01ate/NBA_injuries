from xml.etree import ElementTree
import requests

api_key = 'cvvxw2n26jggmr2py2z8mj26'


if __name__ == '__main__':
    resp = requests.get(f"https://api.sportradar.us/nba/trial/v5/en/league/injuries.xml?api_key={api_key}")
    root = ElementTree.fromstring(resp.content)
    child = list(root)[0]
    print(resp.content)
    for team in child:
        print('Team name: ' + team.get('name'))
        player = list(team)[0]
        print('Injured player: ' + player.get('full_name'))
        injury = list(player)[0]
        print('Injury date: ' + injury.get('start_date'))
        print('Injury: '+ injury.get('desc'))
        print('Comment: ' + injury.get('comment'))
        print('Updated on ' + injury.get('update_date'))
        print('\n')

# Example with other modules may be in Stage1 folder :)