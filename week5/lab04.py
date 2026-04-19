# LAB EXERCISE 04

# SET UP BEGINS - Do Not Modify
movie_data = [
    ["Inception", 2010, 8.8, "Sci-Fi", 829.9],
    ["The Shawshank Redemption", 1994, 9.3, "Drama", 28.3],
    ["The Godfather", 1972, 9.2, "Crime", 134.8],
    ["The Dark Knight", 2008, 9.0, "Action", 1005.0],
    ["The Matrix", 1999, 8.7, "Sci-Fi", 467.2],
    ["Interstellar", 2014, 8.6, "Sci-Fi", 701.8],
    ["Forrest Gump", 1994, 8.8, "Drama", 678.2],
    ["The Lord of the Rings: The Return of the King", 2003, 8.9, "Fantasy",
1142.5],
    ["Pulp Fiction", 1994, 8.9, "Crime", 213.9],
    ["The Lion King", 1994, 8.5, "Animation", 968.5],
    ["Fight Club", 1999, 8.8, "Drama", 101.2],
    ["Gladiator", 2000, 8.5, "Action", 460.5],
    ["Titanic", 1997, 7.9, "Romance", 2187.5],
    ["Jurassic Park", 1993, 8.2, "Adventure", 1045.7],
    ["The Avengers", 2012, 8.0, "Action", 1518.8],
    ["Avatar", 2009, 7.8, "Sci-Fi", 2923.7],
    ["The Silence of the Lambs", 1991, 8.6, "Thriller", 272.7],
    ["Saving Private Ryan", 1998, 8.6, "War", 482.3],
    ["The Departed", 2006, 8.5, "Crime", 291.5],
    ["Whiplash", 2014, 8.5, "Drama", 49.0]
]
# SET UP ENDS - Do Not Modify

# PROBLEM 01
class Movie:
    """
    Represents a movie with basic metadata and performance information.

    Attributes:
        title (str): The title of the movie.
        year (int): The year the movie was released.
        rating (float): The movie's rating (0.0 to 10.0).
        genre (str): The genre of the movie.
        box_office (float): Box office revenue in millions of dollars.

    Methods:
        __init__(): Initializes all movie attributes.
        is_highly_rated(): Returns True if the movie's rating is 8.0 or above,
            False otherwise.
    """
    # Initialize all movie attributes
    def __init__(self, title, year, rating, genre, box_office):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre
        self.box_office = box_office

    # Function which returns T or F based on movie rating
    def is_highly_rated(self):
        if self.rating >= 8:
            return True
        else:
            return False

# PROBLEM 02
def create_movie_objects(lst):
    """
    Create Movie objects from a list of movie data

    parameter: list of lists, where each inner list contains
                [title, year, rating, genre, box_office]
    returns: list of Movie objects
    """
    movie_objects = []
    # Assign each object to corresponding value from list
    for movie in lst:
        title = movie[0]
        year = movie[1]
        rating = movie[2]
        genre = movie[3]
        box_office = movie[4]

        # Call back to class Movie
        movie = Movie(title, year, rating, genre, box_office)

        # Add movie to new list of movie obe=jects
        movie_objects.append(movie)

    return movie_objects

# PROBLEM 03
def get_top_rated_movies(lst, n):
    """
    Create list of top "n" movies from list of movie objects

    parameters: list of Movie objects & an integer n (which represents
                # of top "n" movies
    returns: list of the titles of the top "n" movies, sorted by
                rating (highest to lowest)
    """
    # Sort movies by rating in descending order (highest first)
    sorted_movies = sorted(lst, key = lambda movie: movie.rating, reverse=True)

    # Get top "n" movies (or all if there are fewer than "n")
    top_n_movies = sorted_movies[:n]

    # Get only the titles of top "n" movies
    titles = []
    for movie in top_n_movies:
        titles.append(movie.title)

    return titles

# PROBLEM 04
def analyze_genre(lst, genre):
    """
    Take list of Movie objects & specific genre, then return dictionary
    with key-value pairs representing the # of movies, average rating,
    total box office revenue, and # of highly rated movies in the genre

    parameters: list of Movie objects & a movie genre (string)
    returns: dictionary with keys & value pairs of
            1. count: # of movies in genre
            2. avg_rating: avg. rating of movies in genre (round to 2 decimals)
            3. total_box_office: total box office revenue for that genre (round to 2 decimals)
            4. highly_rated_count: # of highly rated movies in genre
    """
    count = 0
    total_rating = 0
    total_box_office = 0
    highly_rated_count = 0

    # Loop through each movie in list to get each piece of information
    for movie in lst:
        if movie.genre == genre:
            count += 1
            total_rating += movie.rating
            total_box_office += movie.box_office
            if movie.rating >= 8:
                highly_rated_count += 1

    # Handle case where no movies match genre (avoid ZeroDivisionError)
    if count == 0:
        avg_rating = 0
    else:
        avg_rating = round(total_rating / count, 2)

    # Create dictionary with all requested information for genre
    genre_info = {"count": count, "avg_rating": avg_rating,
                  "total_box_office": round(total_box_office, 2),
                  "highly_rated_count": highly_rated_count}
    return genre_info

def main():
    # Problem 1 Testing
    movie = Movie("Inception", 2010, 8.8, "Sci-Fi", 829.9)
    print(movie.title)
    print(movie.is_highly_rated())
    # Problem 2 Testing
    movies = create_movie_objects(movie_data)
    print(movies[0].title)
    # Problem 3 Testing
    data = [Movie("Inception", 2010, 8.8, "Sci-Fi", 829.9),
       Movie("The Matrix", 1999, 8.7, "Sci-Fi", 467.2),
       Movie("Interstellar", 2014, 8.6, "Sci-Fi", 701.8)]
    top_movies = get_top_rated_movies(data, 2)
    print(top_movies)
    top_movies2 = get_top_rated_movies(data, 5)
    print(top_movies2)
    # Problem 4 Testing
    data = [Movie("Inception", 2010, 8.8, "Sci-Fi", 829.9),
       Movie("The Matrix", 1999, 8.7, "Sci-Fi", 467.2),
       Movie("Titanic", 1997, 7.9, "Drama", 2201.6)]
    result = analyze_genre(data, "Sci-Fi")
    print(result)
    result2 = analyze_genre(data, "News")
    print(result2)

if __name__ == '__main__':
    main()