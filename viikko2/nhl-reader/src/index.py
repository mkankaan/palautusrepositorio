from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():
    seasons = ""
    y = 18
    steps = 8

    for i in range(steps):
        seasons += f"20{y}-{y+1}"

        if i < steps-1:
            seasons += "/"
        y += 1
    
    season_list = f"[{seasons}]"
    default_season = "2024-25"
    nationalities = "USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/" \
        "AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS"
    
    console = Console()
    season = console.input(f"Season [purple bold]{season_list}[/] [blue_violet bold]({default_season})[/]: ")

    if season == "":
        season = default_season

    while True:
        nationality = console.input(f"Nationality [purple bold][{nationalities}][/] [blue_violet bold]()[/]: ").upper()

        if nationality == "":
            continue

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

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


if __name__ == "__main__":
    main()
