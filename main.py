import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
web_page = BeautifulSoup(response.content, "html.parser")
all_movies = web_page.find_all(name="h3", class_="title")

with open("movies.txt", mode="w") as file:
    for movie in all_movies[::-1]:
        file.writelines(f"{movie.getText()}\n")