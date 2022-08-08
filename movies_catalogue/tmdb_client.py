import json
import random

import requests
from pprint import pprint
import os
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRkMzBhZjE3NDY4NmQzNzRmMjcxMDRmMjMxOWI0YyIsInN1YiI6IjYyYzU5NzdkYjZjMjY0MDA1MTNlZjAzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ys0Yi7yxgecxolhYTZQzw_feMFrLoSqTx7F329WMSYU"

def get_api_from_tmdb(endpoint):
    url_adres = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url_adres, headers=headers)
    response.raise_for_status()
    return response.json()

def get_top_movies(list_type= "popular"):
    return get_api_from_tmdb(f"movie/{list_type}")

def get_poster(post_path,size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{post_path}"


def get_movies(list_type, amount_of_movies=8):
    movies = []
    list_of_movie = get_top_movies(list_type)['results']
    for _ in range(int(amount_of_movies)):
        movies.append(list_of_movie[_])
    return movies


def get_movie_info(list_type="popular",amount_of_movies=8):
    movies = get_movies(list_type, amount_of_movies)
    movies_posters = {}
    for movie in movies:
        movies_posters.setdefault(movie['title'], get_poster(movie['poster_path'], size="w342"))
    return movies_posters


def get_single_movie(movie_id):
    return get_api_from_tmdb(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    return get_api_from_tmdb(f"movie/{movie_id}/credits")["cast"]


def searcher(search_query):
    endpoint = f"search/movie/?query={search_query}"
    return get_api_from_tmdb(endpoint)['results']

def get_tv_series(amount=8):
    tv_series_list=[]
    endpoint = "tv/airing_today"
    tv_series = get_api_from_tmdb(endpoint)['results']
    random.shuffle(tv_series)
    for _ in range(amount):
        tv_series_list.append(tv_series[_])
    return tv_series_list




