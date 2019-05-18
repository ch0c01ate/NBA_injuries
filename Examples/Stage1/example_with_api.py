from nba_api.stats.endpoints import playercareerstats
import json


def get_year():
    year = input("")
    try:
        year = int(year)

        if(2002<year<2019):
            year2 = year % 100 + 1
            return str(year) + '-' + str(year2)

        else:
            print("Wrong data")

    except:
        print("Wrong data")


def main():
    player_stats = json.loads(playercareerstats.PlayerCareerStats(player_id=2544).get_json())
    headers = player_stats["resultSets"][0]["headers"]
    row_set = player_stats["resultSets"][0]["rowSet"]

    print("Enter first year of the season to get stats for. It should be between 2003 and 2018:")
    year = get_year()

    for r in row_set:
        if year == r[1]:
            row = r
            break

    print("Here is stats for Lebron James for", year, "season:")
    for i in range(len(headers)):
        print(headers[i], '-', row[i])


if __name__ == '__main__':
    main()