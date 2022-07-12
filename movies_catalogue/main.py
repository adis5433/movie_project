from flask import Flask, render_template, request, redirect
import requests
from tmdb_client import get_poster, get_movies, get_single_movie,get_single_movie_cast

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return redirect("/")


@app.route('/')
def homepage():
    movies_types_of_lists = {"Popular": "popular", "Top Rated ": "top_rated", "Upcoming": "upcoming"}
    selected_list = request.args.get('list_type', 'popular')
    movies = get_movies(list_type=selected_list)
    if selected_list not in movies_types_of_lists.values():
        return render_template("homepage.html", movies=movies, current_list='popular', movies_types_of_lists= movies_types_of_lists)
    return render_template("homepage.html", movies=movies, current_list=selected_list, movies_types_of_lists= movies_types_of_lists)




@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = get_single_movie(movie_id)
    cast = get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)


@app.context_processor
def utility_procesor():
    def tmdb_img_url(path, size):
        return get_poster(path, size)
    return {"tmdb_img_url": tmdb_img_url}





if __name__ == '__main__':
    app.run(debug=True)