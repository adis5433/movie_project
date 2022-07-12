import json
import random

import requests
from pprint import pprint
from random import Random
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRkMzBhZjE3NDY4NmQzNzRmMjcxMDRmMjMxOWI0YyIsInN1YiI6IjYyYzU5NzdkYjZjMjY0MDA1MTNlZjAzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ys0Yi7yxgecxolhYTZQzw_feMFrLoSqTx7F329WMSYU"

def get_top_movies(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster(post_path,size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{post_path}"


def get_movies(list_type, amount_of_movies=8):
    movies = []
    for _ in range(int(amount_of_movies)):
        movies.append(get_top_movies(list_type)['results'][_])
    return movies


def get_movie_info():
    movies = get_movies()
    movies_posters = {}
    for movie in movies:
        movies_posters.setdefault(movie['title'], get_poster(movie['poster_path'], size="w342"))
    return movies_posters


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "Authorization": f"Bearer {api_token}",

    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]




movie = get_single_movie(13)
cast = get_single_movie_cast(13)
print(get_top_movies('popular'))
print(cast)
print(movie["budget"])
print(get_poster('36qWnokCU1VOdSyrmGbTxzGou44.jpg', 'w185'))