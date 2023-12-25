def main():
    scores_info = {
        "First Team": 100,
        "Second Team": 90,
        "Third Team": 80,
        "Fourth Team": 50,
        "Fifth Team": 30,
    }
    team_list = [input(f"{i+1}. Enter team name (First Team, Second Team, Third Team, Fourth Team, Fifth Team): \n") for i in range(5)
                 ]
    if position_checker(scores_info, team_list):
        print("Team positions correct!")
    else:
        print("Team positions incorrect!")


def position_checker(scores_info: dict, team_list: list) -> bool:
    sorted_teams = sorted(scores_info.keys(), key=lambda x: scores_info[x], reverse=True)
    return sorted_teams == team_list


if __name__ == '__main__':
    main()
