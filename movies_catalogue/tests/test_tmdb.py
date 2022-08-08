from main import app
import tmdb_client
from unittest.mock import Mock
import pytest


example_movie_id = 13


def test_get_top_popular_movies(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_top_movies(list_type="popular")
   assert movies_list == mock_movies_list



def test_get_movie_info():
   movie_posters = tmdb_client.get_movie_info()
   assert movie_posters is not None

def test_getting_cast():
   cast = tmdb_client.get_single_movie_cast(example_movie_id)
   assert cast is not None


@pytest.mark.parametrize("list_type, statuscode",(
        ("/?list_type=popular", 200),
        ("/?list_type=top_rated", 200),
        ("/?list_type=upcoming", 200),
        ("/?list_type=now_playing", 200),
         ))
def test_views(list_type, statuscode):

   with app.test_client() as client:
        response = client.get(list_type)
        assert response.status_code == statuscode


