# LAB EXERCISE 05
import requests
from bs4 import BeautifulSoup

### SET UP BEGINS Do not modify
punctuations = ["", "—", ":"]

city_locations = [
    {"name": "Boston", "latitude": 42.36, "longitude": -71.06},
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "Fake City", "latitude": 999, "longitude": -999}
]
### SET UP ENDS Do not modify

# PROBLEM 01
def scrape_quotes_by_author(num_pages):
    """
    Scrapes quotes from URL & returns dictionary mapping
    author names to a list of their quotes

    Parameters: num_pages (int) - # of pages to scrape

    Returns: dictionary - keys are author names, values
                          are list of quotes by that author
    """
    author2quotes = {}

    for page in range(1, num_pages + 1):
        base_url = f"https://quotes.toscrape.com/page/{page}"
        response = requests.get(base_url)

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote blocks using class="quote"
        quote_blocks = soup.find_all("div", class_="quote")

        # If no quotes found, we've reached the last page
        if not quote_blocks:
            break

        for block in quote_blocks:
            # Extract quote text using find() w/ tag & class
            text = block.find("span", class_="text").text.strip()

            # Extract author using same method as quote
            author = block.find("small", class_="author").text.strip()

            # Add quotes to corresponding author
            if author not in author2quotes:
                author2quotes[author] = []
            author2quotes[author].append(text)

    return author2quotes

# PROBLEM 02
def scrape_study_abroad_countries():
    """
    Scrapes Northeastern course catalog & returns list of unique
    countries mentioned in "International Study" course titles

    Returns: list - unique country names found in abroad course titles
    """

    url = "https://catalog.northeastern.edu/course-descriptions/abrd/"
    response = requests.get(url)

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all course title blocks (inspect page to find right tag/class)
    course_titles = soup.find_all("p", class_="courseblocktitle noindent")

    countries = []

    for course in course_titles:
        text = course.text.strip()
        
        if "International Study" in text:
            # Split text on "International Study" to get country half of text (right side)
            country_part = text.split("International Study")[1].strip()

            # Split on period "." to remove everything to right of country
            country = country_part.split(".")[0].strip()

            # Clean country using punctuation list
            for p in punctuations:
                country = country.replace(p, "").strip()

            # Only add unique countries to list
            if country not in countries:
                countries.append(country)

    return countries

# PROBLEM 03
def get_weather_summary(cities):
    """
    Retrieves current weather information from open API for a list of cities

    Parameters: cities (list of dictionaries) - each contains "name",
                "latitude", "longitude"

    Returns: dictionary - keys are city names, values are dictionaries
             with "temperature", "windspeed", & "weathercode"
    :return:
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    weather_summary = {}

    for city in cities:
        # Extract city name from dictionary
        name = city["name"]

        # Pass query parameters to API
        params = {
            "latitude": city["latitude"],
            "longitude": city["longitude"],
            "current_weather": True
        }

        try:
            # Convert response to python dictionary
            response = requests.get(base_url, params=params)
            response_dict = response.json()
            print(response_dict)

            # Navigate nested dictionary to get the weather data
            current = response_dict["current_weather"]

            weather_summary[name] = {
                "temperature": float(current["temperature"]),
                "windspeed": float(current["windspeed"]),
                "weathercode": int(current["weathercode"])
            }

        # If an error occurs, store "NA" for all fields
        except Exception:
            weather_summary[name] = {
                "temperature": "NA",
                "windspeed": "NA",
                "weathercode": "NA"
            }

    return weather_summary

def main():
    # Problem 1 testing
    result = scrape_quotes_by_author(3)
    print(result)

    # Problem 2 testing
    result2 = scrape_study_abroad_countries()
    print(result2)

    # Problem 3 testing
    print(get_weather_summary(city_locations))

if __name__ == '__main__':
    main()