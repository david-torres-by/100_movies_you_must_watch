from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
movies_api = response.text

soup = BeautifulSoup(movies_api, "html.parser")

# title for the txt
txt_title = soup.title.string

# 100 movies worth to watch titles:
tags_list = soup.find_all(name='a', class_='xs-text-charcoal decoration-none')
movies_list = []

for item in tags_list:
	movies_list.append(item.string)

movies_rankings_list = []

for movie in movies_list:
	movies_rankings_list.append(movie.strip())

movies_rankings_list2 = []

with open("100 Movies to watch!.txt", "w", encoding="utf-8") as text_file:
	for movie in movies_rankings_list:
		movies_rankings_list2.append(movie.replace("xa0", ""))
		text_file.write(f"Movie Title: {movie}\n")

print(text_file.readlines())

