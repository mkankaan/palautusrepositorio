from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def get_season_list():
    seasons = ""
    year = 18
    steps = 8

    for i in range(steps):
        seasons += f"20{year}-{year+1}"

        if i < steps-1:
            seasons += "/"
        year += 1
    return seasons


def get_season():
    console = Console()
    season_list = get_season_list()
    default_season = "2024-25"
    season = console.input(f"Season [purple bold][{season_list}][/] \
                           [blue_violet bold]({default_season})[/]: ")
    return default_season if season == "" else season


def get_nationality():
    console = Console()
    nationality_list = "USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/" \
        "AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS"
    nationality = ""

    while nationality == "":
        nationality = console.input(f"Nationality [purple bold][{nationality_list}][/] \
                                    [blue_violet bold]()[/]: ")
    return nationality.upper()


def show_table(players, season, nationality):
    console = Console()
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Released", style="blue_violet")
    table.add_column("teams", style="purple")
    table.add_column("goals", style="cyan")
    table.add_column("assists", style="cyan")
    table.add_column("points", style="cyan")

    for player in players:
        table.add_row(player.name, player.team, str(player.assists),
                        str(player.goals), str(player.assists + player.goals))
    console.print(table)


def get_stats(season, nationality):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(nationality)


def main():
    season = get_season()

    while True:
        nationality = get_nationality()
        players = get_stats(season, nationality)
        show_table(players, season, nationality)


if __name__ == "__main__":
    main()
