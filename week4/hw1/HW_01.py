# """
# Santiago Cuervo
# DS 2500
# Homework 1
# January 27, 2026
# HW_01.py
# """

# import library
import csv

# PROBLEM 1
def load_pixar_data(filename):
    """
    Loads Pixar films data from a CSV file.

    Args:
    filename (str): Path to the CSV file containing Pixar films data.

    Returns:
    data (list): List of dictionaries with film data.
    """
    data = []
    # Open csv file & convert data into a list
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    # Error handling
    except FileNotFoundError:
        print(f"File: {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    # Return pixar data as a list of dictionary objects
    return data

def clean_pixar_data(data):
    """
    Cleans Pixar films data from a CSV file.
    Removes rows with empty string value in 'film'.
    Converts numeric fields ('run_time', 'rotten_tomatoes',
    'metacritic') to float if they are not empty strings.

    Args:
    data (list): list of dictionaries

    Returns:
    tuple: a tuple containing:
        - clean_data_list (list): List of dictionaries with cleaned film data.
        - original_count (int): Integer of original number of rows in the CSV file.
        - removed_count (int): Integer of number of rows removed due to missing data.
        - final_count (int): Integer of final number of rows after cleaning.
    """
    original_count = len(data)
    clean_data_list = []
    removed_count = 0

    for row in data:
        if row['film'] == '':
            removed_count += 1
            # Skip row entirely
            continue

        # Convert numeric fields to floats, leave others as strings
        clean_row = {
            'number': row['number'],
            'film': row['film'],
            'release_date': row['release_date'],
            'run_time': float(row['run_time']) if row['run_time'] != '' else
            None,
            'film_rating': row['film_rating'],
            'rotten_tomatoes': float(row['rotten_tomatoes']) if
            row['rotten_tomatoes'] != '' else None,
            'metacritic': float(row['metacritic']) if row['metacritic'] != ''
            else None
        }
        # Add row to cleaned data list
        clean_data_list.append(clean_row)

    final_count = len(clean_data_list)
    # Return a tuple containing key information
    return (clean_data_list, original_count, removed_count, final_count)

# PROBLEM 2
def calculate_rt_score_statistics(data):
    """
    Analyzes Pixar films data to calculate Rotten Tomatoes scores statistics.
    Cannot use sort(), min(), max(), mean(), or sum() functions.
    Can use round() function to round the average score to 1 decimal place.

    Args:
    data (list): List of dictionaries containing cleaned Pixar films data.

    Returns:
    dictionary: A dictionary containing the following keys and values:
        - min_score (float): Minimum Rotten Tomatoes score.
        - max_score (float): Maximum Rotten Tomatoes score.
        - avg_score (float): Average Rotten Tomatoes score rounded to 1 decimal place.
    """
    min_score = 100.0
    max_score = 0.0
    total_scores = 0.0
    count = 0

    # Loop through scores
    for row in data:
        score = row['rotten_tomatoes']
        # Skip None values
        if score is not None:
            # Set max and min scores to highest/lowest values
            if score > max_score:
                max_score = score
            if score < min_score:
                min_score = score
            total_scores += score
            count += 1

    # Calculate + round average score to 1st decimal
    avg_score = round(total_scores / count, 1) if count > 0 else None

    return {
        'min_score': min_score,
        'max_score': max_score,
        'avg_score': avg_score
            }

# PROBLEM 3
# SETUP
num2month = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

# END SETUP

def get_most_popular_release_month(data):
    """
    Returns the most popular release month and the number of films released in that month.
    max() or sort() functions cannot be used.

    Args:
    data (list): List of dictionaries containing cleaned Pixar films data.

    Returns:
    tuple: A tuple containing:
        - most_popular_month (str): The month with the highest number of films released.
                                    The month is represented as a string (e.g., "January").
        - total_films (int): The total number of films released in that month.
    """
    pass  # TODO implement

    most_popular_month = ""
    total_films = 0

    # Film count for each month using "num2month" keys
    month_counts = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                    '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, }

    # Loop through data to get month
    for row in data:
        date = row['release_date']
        month_num = date[5:7]
        month_counts[month_num] += 1

    # Loop to find month w/ most films
    for month_num in num2month:
        if month_counts[month_num] > total_films:
            total_films = month_counts[month_num]
            most_popular_month = num2month[month_num]

    return (most_popular_month, total_films)

# PROBLEM 4(a)
def get_longest_and_shortest_films(data):
    """
    Analyzes Pixar films data to find the longest and shortest films.
    max(), min(), and sort() functions cannot be used.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with the following keys and values:
        - shortest_film (str): The title of the shortest film.
        - longest_film (str): The title of the longest film.
    """
    shortest_film = ""
    shortest_length = 200
    longest_film = ""
    longest_length = 0

    # Loop through each film's run time in the data
    for row in data:
        run_time = row['run_time']
        if run_time is not None:
            # Set longest + shortest films to correct film
            if run_time < shortest_length:
                shortest_film = row['film']
                # Update length
                shortest_length = run_time
            if run_time > longest_length:
                longest_film = row['film']
                # Update length
                longest_length = run_time

    return {
        'shortest_film': shortest_film,
        'longest_film': longest_film,
    }

# PROBLEM 4(b)
def get_runtime_category_counts(data):
    """
    Analyzes Pixar films data to categorize runtimes and count occurrences.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with runtime categories as keys and their counts as values.
        - 'short': Count of films with runtime < 90 minutes
        - 'medium': Count of films with runtime between 90 and 110 minutes (inclusive)
        - 'long': Count of films with runtime > 110 minutes
    """
    short = 0
    medium = 0
    long = 0

    # Loop through film's runtimes to classify each
    # as either short, medium, or long in length
    for row in data:
        run_time = row['run_time']
        if run_time is not None:
            if run_time < 90:
                short += 1
            elif run_time <= 110:
                medium += 1
            else:
                long += 1

    return {
        'short': short,
        'medium': medium,
        'long': long
    }

# PROBLEM 4(c)
def get_runtime_by_rating(data, rating):
    """
    Returns the average runtime of films with a specific rating (e.g., 'G', 'PG', 'PG-13', 'R').
    Returns None if the rating is not valid or if there are no films with that rating.
    Can use round() function to round the average score to 1 decimal place.

    Args:
    data (list): List of dictionaries containing Pixar films data.
    rating (str): The film rating to filter by (options can be: 'G', 'PG', 'PG-13', 'R').

    Returns:
    float: The average runtime of films with the specified rating. Rounded to 1 decimal place.
    """
    total_run_time = 0
    count = 0

    # Loop through data to get avg. runtime for specific film rating
    for row in data:
        film_rating = row['film_rating']
        if film_rating == rating:
            total_run_time += row['run_time']
            count += 1
    # Round average to first decimal place & handle "None" cases
    return round(total_run_time / count, 1) if count > 0 else None

# PROBLEM 5(a)
def get_films_by_type(data, type_filter):
    """
    Filters the Pixar films data to get a list films by type (either 'original' or 'sequel').
    Sequels are films that are not original and can be the second or later in a series.
    Use remove_punctuation_and_articles function implemented above as a helper function.

    Args:
    data (list): List of dictionaries containing Pixar films data.
    type_filter (str): The type of film to filter by ('original' or 'sequel').

    Returns:
    list: A list of dictionaries containing only original films.
    """
    originals = []
    sequels = []

    # Loop through each film to check earlier films
    for i in range(len(data)):
        current_row = data[i]
        current_film = current_row['film']
        current_year = current_row['release_date'][:4]

        is_sequel = False

        # Check if current film is a sequal to any earlier film
        # (Only look at films released before current film)
        for j in range(i):
            prev_row = data[j]
            prev_film = prev_row['film']
            prev_year = prev_row['release_date'][:4]

            # Split previous films into words
            # EX: "Toy Story 3" -> ["Toy", "Story", "3"]
            prev_words = prev_film.split()
            for word in prev_words:
                # Clean punctuation from word
                # EX: "Monsters," -> "Monsters"
                word = word.replace(",", "")
                # Film is sequel if: released later AND
                # shares significant word with original
                # (Ignore very short words - EX: "the")
                if (int(current_year) > int(prev_year) and
                word in current_film and
                len(word) > 3):
                    is_sequel = True
                    break
            if is_sequel:
                break

        # Add film to list based on whether a sequel or iginal
        if is_sequel:
            sequels.append(current_row)
        else:
            originals.append(current_row)

    if type_filter == "original":
        return originals
    elif type_filter == "sequel":
        return sequels
    else:
        return None

# PROBLEM 5(b)
def calculate_originals_and_sequels_rt_scores(data):
    """
    Calculate the originals and sequels average Rotten Tomatoes scores.
    Uses the get_films_by_type functions to filter the data.
    Use lambda function which uses sum() to calculate the average RT score.
    Can use round() function to round the average score to 1 decimal place.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with the following keys and values:
        - original_avg_rt_score (float): Average Rotten Tomatoes score for original films. Rounded to 1 decimal place.
        - sequel_avg_rt_score (float): Average Rotten Tomatoes score for sequels. Rounded to 1 decimal place.
    """
    # Call to get_films_by_type function from 5(a)
    originals = get_films_by_type(data, "original")
    sequels = get_films_by_type(data, "sequel")
    original_scores = 0
    original_count = 0
    sequel_score = 0
    sequel_count = 0

    # Loop through original films to get their combined total scores
    # on rotten tomatoes & # of original films
    for row in originals:
        score = row['rotten_tomatoes']
        if score is not None:
            original_scores += score
            original_count += 1

    # Loop through sequel films & do same as original films above
    for row in sequels:
        score = row['rotten_tomatoes']
        if score is not None:
            sequel_score += score
            sequel_count += 1

    # Round average rotten tomatoes scores to first decimal place
    # and return both in dictionary & key format
    return {
            'original_avg_rt_score': round(original_scores / original_count, 1) if original_count > 0 else None,
            'sequel_avg_rt_score': round(sequel_score / sequel_count, 1) if sequel_count > 0 else None
        }

# PROBLEM 6
def filter_top_five_films(data):
    """
    Filter the top five films based on their composite scores.
    This function should use lambda function for calculating the composite score.
    Use map() and sorted() to help sort your data based on composite score.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    list: A list of dictionaries containing the top five films with their composite scores.
          The list is sorted in descending order by composite score. The dictionary contains:
            - 'film': The title of the film.
            - 'composite_score': The composite score of the film.
    """
    films_scores = []

    # Loop through rotten tomatoes & metacritic scores of each film
    # (Handles None values)
    for row in data:
        if row['rotten_tomatoes'] is None:
            rt = 0
        else:
            rt = row['rotten_tomatoes']

        if row['metacritic'] is None:
            meta = 0
        else:
            meta = row['metacritic']

        # Composite score formula
        composite = (rt * 0.4) + (meta * 0.6)

        # Create list of all film's composite score
        films_scores.append({'film': row['film'],
                             'composite_score': composite
                             })

    # Sort list by composite score (descending order)
    sorted_scores = sorted(films_scores, key = lambda x: x['composite_score'],
                                reverse = True)

    # Only return the top 5 highest scores
    return sorted_scores[:5]

if __name__ == "__main__":
    print("HW 01: PIXAR FILMS DATA ANALYSIS")

    # Use this main function to call your functions and test them.

    # PROBLEM 1 - calling
    print('\nProblem 1')
    pixar_data = load_pixar_data('pixar_films.csv')
    print(pixar_data)
    clean_result = clean_pixar_data(pixar_data)
    clean_data = clean_result[0]
    counts = clean_result[1:4]
    print(clean_data)
    print(len(clean_data))
    print(counts)

    # PROBLEM 2 - calling
    print("\nProblem 2")
    stats = calculate_rt_score_statistics(clean_data)
    print(stats)

    # Problem 3 - calling
    print("\nProblem 3")
    months = get_most_popular_release_month(clean_data)
    print(months)

    # Problem 4 - calling
    print("\nProblem 4")
    films = get_longest_and_shortest_films(clean_data)
    print(films)
    length = get_runtime_category_counts(clean_data)
    print(length)
    by_rating = get_runtime_by_rating(clean_data, "PG")
    by_rating2 = get_runtime_by_rating(clean_data, "G")
    print(by_rating)
    print(by_rating2)

    # Problem 5 - calling
    print("\nProblem 5")
    ogs = get_films_by_type(clean_data, "original")
    news = get_films_by_type(clean_data, "sequel")
    print(ogs)
    print(news)
    rotten_tomatoes = calculate_originals_and_sequels_rt_scores(clean_data)
    print(rotten_tomatoes)

    # PROBLEM 6 - calling
    print("\nProblem 6")
    top_five = filter_top_five_films(clean_data)
    print(top_five)