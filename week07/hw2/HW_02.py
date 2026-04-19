import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt

class Team:
    def __init__(self, name):
        # string: team name
        self.name = name
        # list of ints: # of goals scored per game
        self.goals = []

    def add_goals(self, goals):
        """
        Append given goals (int) to team's goals list
        """
        self.goals.append(goals)

    def get_total_goals(self):
        """
        Return total goals scored (int)
        """
        return sum(self.goals)

    def __str__(self):
        return f"Team Name: {self.name}"

def read_data(filename):
    """
    Reads WSL goals data from a csv file & returns a list of Team objects
    Each row represents one team's goals scored per game in the 2023-2024 season
    Empty cells (no goals scored) are converted to 0

    Parameters: file name
    Returns: list of team objects after reading csv file
    """
    teams = []
    # Load csv file into pandas DataFrame (like a table)
    df = pd.read_csv(filename)

    # Loop through each row/team
    for idx, row in df.iterrows():
        # First column is team name, create Team object with it
        team = Team(row.iloc[0])

        # Loop through remaining columns (game's goals)
        for value in row.iloc[1:]:
            # If cell is empty (team didn't score)
            if pd.isna(value):
                # Conver to 0
                team.add_goals(0)
            else:
                # Otherwise, add goal count
                team.add_goals(int(value))

        # Add Team object to list of teams
        teams.append(team)

    # Return full list of Team objects
    return teams

# Function 1
def get_team_with_most_goals(teams):
    """
    Takes in a list of team objects & returns a tuple containing the name
    & total goals of the team that scored the most goals in the season

    Parameters: list of team objects
    Returns: tuple of name & total goals of team that scored
             the most goals in the season
    """
    most_goals = 0

    for team in teams:
        # Check if team scored the most goals
        if team.get_total_goals() > most_goals:
            most_goals = team.get_total_goals()
            team_name = team.name

    return team_name, most_goals

# Function 2
def get_mean_season_goals(teams):
    """
    Takes in list of team objects & returns average (mean) across
    teams of total goals scored during the season

    Parameters: list of team objects
    Returns: average of total goals scored during the season
             across all teams
    """
    all_goals = 0

    for team in teams:
        # Sum total goals across all teams
        all_goals += team.get_total_goals()

    # Formula to calculate for mean
    return round(all_goals / len(teams), 2)

# Function 3
def get_variance_season_goals(teams):
    """
    Takes in a list of team objects & returns the population variance
    of total goals scored during the season

    Parameters: list of team objects
    Returns: population variance of total goals scored during
             the season
    """
    pop_variance_numerator = 0
    # Use prior function to get mean total goals to use in for loop
    mean = get_mean_season_goals(teams)

    for team in teams:
        team_goals = team.get_total_goals()
        # Sum the total squared differences
        pop_variance_numerator += (team_goals - mean) ** 2

    # Divide by "N" for population variance
    return round(pop_variance_numerator / len(teams), 2)

# Function 4
def get_standard_deviation_season_goals(teams):
    """
    Takes in list of team objects & returns the population standard
    deviation of total goals scored during the season

    Parameters: list of team objects
    Returns: population standard deviation of total goals scored
             during the season (allowed to use math.sqrt function)
    """
    variance = get_variance_season_goals(teams)
    # Standard deviation formula
    std_dev = sqrt(variance)

    return round(std_dev, 2)

# Function 5
def get_median_for_team(name, teams):
    """
    Takes in team name & list of team objects & returns the median
    of goals scored by the specified team

    Parameters: team name, list of team objects
    Returns: median of goals scored by specified team (float)
    """
    for team in teams:
        # Find the team that matches input
        if team.name == name:
            # Sort goals list from least to greatest # of goals scored in a game
            sorted_goals = sorted(team.goals)
            n = len(sorted_goals)

            if n % 2 == 0:
                # Formula for calculating median if even # of games
                median = (sorted_goals[n // 2 - 1] + sorted_goals[n // 2]) / 2
            else:
                # Formula for calculating median if odd # of games
                median = sorted_goals[n // 2]

    return median

# Function 6
def get_mode_for_team(name, teams):
    """
    Takes in team name & list of team objects & returns the mode of
    goals scored by the specified team

    Parameters: team name, list of team objects
    Returns: mode of goals scored by specified team
    """
    for team in teams:
        # Find team that matches input
        if team.name == name:
            # Dictionary to store {# of goals: count}
            counts = {}

            for goal in team.goals:
                if goal in counts:
                    # Increment if # of goals already seen
                    counts[goal] += 1
                else:
                    # Initialize # of goals if first time seeing value
                    counts[goal] = 1

    # Return key with the highest count (mode)
    return max(counts, key=counts.get)

# Function 7
def get_most_consistent_team(teams):
    """
    Takes in list of team objects and returns tuple consisting of name
    and coefficient of variation of team with most consistent goal-scoring pattern
    Coefficient of variation = standard deviation / mean

    Parameters: list of team objects
    Returns: tuple with name and coefficient of variation of most
             consistent goal-scoring team
    """
    # Start at infinity, so any coefficient of variation is smaller
    min_co_var = float('inf')
    team_name = ""

    for team in teams:
        # Calculate mean goals per game for each team
        mean = team.get_total_goals() / len(team.goals)
        # Add squared differences and divide by total # of games
        variance = sum((g - mean) ** 2 for g in team.goals) / len(team.goals)
        # Standard deviation formula
        std_dev = variance ** 0.5
        # Coefficient of variation formula
        co_var = std_dev / mean

        # Lower coefficient of variation = more consistent
        if co_var < min_co_var:
            min_co_var = co_var
            team_name = team.name

    return team_name, round(min_co_var, 2)

# Function 8
def get_longest_streak_team(teams):
    """
    Takes in list of team objects and returns a tuple consisting of
    the name and streak length of the team with the longest consecutive
    streak of games where they scored at least 2 goals a game

    Parameters: list of team objects
    Returns: tuple containing name and streak length of team w/ the
             longest consecutive streak of games w/ 2+ goals
    """
    max_streak = 0
    team_name = ""

    for team in teams:
        # Reset streak for each team
        current_streak = 0

        for goals in team.goals:
            if goals >= 2:
                # Extend streak for every consecutive 2+ goals game from team
                current_streak += 1
            else:
                # Reset streak if in game, team scored less than 2 goals
                current_streak = 0

            # Check if current streak is new longest
            if current_streak > max_streak:
                max_streak = current_streak
                team_name = team.name

    return team_name, max_streak

# Function 9
def get_most_improved_mean_goals_team(teams):
    """
    Takes in list of team objects and returns a tuple consisting of name
    and improvement in mean goals of the team that improved their average
    goals per game most from the first half to second half of the season
    Assume: season has  fixed length equal to # of games in original data table

    Parameters: list of team objects
    Returns: tuple with name and improvement in meal goals of most
             improved team from first half to second half of season
    """
    # Negative infinity to make sure improvement is greater than initial value
    max_improvement = float('-inf')
    team_name = ""

    for team in teams:
        # Get midpoint of season
        half = len(team.goals) // 2
        # Team's first half of the season goals
        first_half = team.goals[:half]
        # Team's second half of the season goals
        second_half = team.goals[half:]

        # Team's first half goals meab
        first_mean = sum(first_half) / len(first_half)
        # Team's second half goals mean
        second_mean = sum(second_half) / len(second_half)
        # Formula for tea, improvement
        improvement = second_mean - first_mean

        # Get largest improvement by a team from first to second half
        if improvement > max_improvement:
            max_improvement = improvement
            team_name = team.name

    return team_name, round(max_improvement, 2)

# Function 10 - extra information (abbreviations & colors)
ABBR_MAP = {
    "Arsenal": "ARS",
    "Aston Villa": "AVL",
    "Brighton and Hove Albion": "BHA",
    "Bristol City": "BCFC",
    "Chelsea": "CHE",
    "Everton": "EFC",
    "Leicester City": "LCFC",
    "Liverpool": "LFC",
    "Manchester City": "MCFC",
    "Manchester United": "MUFC",
    "Tottenham Hotspur": "THFC",
    "West Ham United": "WHU"
}
COLOR_MAP = {
    "Arsenal": "red",
    "Aston Villa": "lightskyblue",
    "Brighton and Hove Albion": "mediumblue",
    "Bristol City": "darkred",
    "Chelsea": "blue",
    "Everton": "darkblue",
    "Leicester City": "orange",
    "Liverpool": "orangered",
    "Manchester City": "steelblue",
    "Manchester United": "yellow",
    "Tottenham Hotspur": "navy",
    "West Ham United": "brown"
}

# Function 10
def plot_teams(teams):
    """
    Takes in list of team objects and generates an animated scatter
    plot of each team's goal progression throughout the 2023-2024 season.
    For each game of the season, it should render a new plot showing
    all team''s positions, updating each team's x-value by the #
    of goals they scored in that game. It should look like a mini-animation

    Parameters: list of team objects
    Returns: animated scatter plot of each team's goal progression
             throughout the season
    """
    # Every team has same # of games in season so can use any team (EX: teams[0])
    num_games = len(teams[0].goals)
    # Find max # of goals scored by a team (x-axis limit)
    max_goals = max(team.get_total_goals() for team in teams)

    # Show plot without interrupting code execution
    plt.show(block=False)

    # Give plot a wider figure
    plt.figure(figsize=(14, 7))

    # Loop through each game
    for game in range(num_games + 1):
        # Clear previous plot
        plt.clf()

        for i, team in enumerate(teams):
            # total goals up until current game
            cumulative = sum(team.goals[:game])

            # x-axis = total goals, y-axis = each team's row
            # full name + abbreviation in legend
            # right-pointing triangle instead of dot
            # set marker size to 100
            plt.scatter(cumulative, i,
                        color=COLOR_MAP[team.name],
                        label=f"{team.name} ({ABBR_MAP[team.name]})",
                        marker=">",
                        s=100)

        # y-axis: one row per team, labeled by corresponding abbreviation
        plt.yticks(range(len(teams)), [ABBR_MAP[team.name] for team in teams])
        # x-axis: ticks by 10
        plt.xticks(range(0, max_goals + 10, 10))

        # x-axis range
        plt.xlim(0, max_goals + 10)
        plt.xlabel("Cumulative Goals Scored")
        plt.ylabel("Teams")
        # Centered title
        plt.title(f"WSL 2023-2024 Goal Progression - Game: {game}", loc="center")
        # Place the legend outside the plot in the middle right area
        plt.legend(loc="upper left", bbox_to_anchor=(1, 0.75))
        # Prevent parts of the plot getting cut off at edges (legend or axis labels)
        plt.tight_layout()
        # Pause between each frame of team's total goals by game
        plt.pause(0.5)

    # Keep final plot open at the end
    plt.show()

# Main function
def main():
    # Testing read file function
    teams = read_data("wsl_goals_2324.csv")
    # Testing function 1
    name, goals = get_team_with_most_goals(teams)
    print(f"Team with most goals: {name}\nTheir total goals: {goals}")
    # Testing function 2
    average = get_mean_season_goals(teams)
    print(f"Mean total goals per team this season: {average}")
    # Testing function 3
    variance = get_variance_season_goals(teams)
    print(f"Population variance of total goals scored during this season: {variance}")
    # Testing function 4
    std_dev = get_standard_deviation_season_goals(teams)
    print(f"Population standard deviation of total goals scored during this season: {std_dev}")
    # Testing function 5
    team_name = "Arsenal"
    median = get_median_for_team(team_name, teams)
    print(f"{team_name}'s median goals scored is {median}")
    # Testing function 6
    team_name2 = "Tottenham Hotspur"
    mode = get_mode_for_team(team_name2, teams)
    print(f"{team_name2}'s mode goals scored is {mode}")
    # Testing function 7
    name, co_var = get_most_consistent_team(teams)
    print(f"{name} is the most consistent team with a coefficient of variation of {co_var}")
    # Testing function 8
    name, streak = get_longest_streak_team(teams)
    print(f"{name} had the longest consecutive streak of games where"
          f" they scored at least 2 goals per game at {streak} games")
    # Testing function 9
    name, improvement = get_most_improved_mean_goals_team(teams)
    print(f"{name} had the most improved average goals per game from "
          f"the first half to second half of the season at +{improvement}")
    # Testing function 10
    plot_teams(teams)

if __name__ == '__main__':
    main()