import json
import random

import requests
from pprint import pprint
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRkMzBhZjE3NDY4NmQzNzRmMjcxMDRmMjMxOWI0YyIsInN1YiI6IjYyYzU5NzdkYjZjMjY0MDA1MTNlZjAzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ys0Yi7yxgecxolhYTZQzw_feMFrLoSqTx7F329WMSYU"


def get_top_movies(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response_list = response.json()['results']
    random.shuffle(response_list)
    return response_list


def get_poster(post_path,size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{post_path}"


def get_movies(list_type, amount_of_movies=8):
    movies = []
    list_of_movie = get_top_movies(list_type)
    for _ in range(int(amount_of_movies)):
        movies.append(list_of_movie[_])
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


def searcher(search_query):
    beginning_of_url = f"https://api.themoviedb.org/3/"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    endpoint = f"{beginning_of_url}search/movie/?query={search_query}"
    response = requests.get(endpoint, headers=headers)
    return response.json()['results']

def get_tv_series(amount=8):
    tv_series_list=[]
    endpoint = "https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    tv_series = response.json()['results']
    random.shuffle(tv_series)
    for _ in range(amount):
        tv_series_list.append(tv_series[_])
    return tv_series_list





print(get_single_movie(24))