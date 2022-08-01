from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for, flash
import requests
import datetime
from tmdb_client import get_poster, get_movies, get_single_movie,get_single_movie_cast, searcher, get_tv_series

app = Flask(__name__)
movies_types_of_lists = {
        "Popular": "popular", "Top Rated ": "top_rated", "Upcoming": "upcoming", "Now playing": "now_playing"
    }
FAVORITES = set()
print(FAVORITES)
app.secret_key = b'flask_secret_key'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in movies_types_of_lists.values():
        return redirect(url_for('homepage'))
    movies = get_movies(list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, movies_types_of_lists= movies_types_of_lists)



@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = get_single_movie(movie_id)
    cast = get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)


@app.route("/favorites")
def show_favorites():
    movies = []
    if FAVORITES:
        for movie_id in FAVORITES:
            movie_data = get_single_movie(movie_id)
            print(movie_data)
            movies.append(movie_data)
    print(url_for('tv_series'))
    print(url_for(request.endpoint))
    return render_template("favorites.html", movies=movies, movies_types_of_lists=movies_types_of_lists,
                           current_list=url_for(request.endpoint))


@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie = get_single_movie(movie_id)
    if movie_id:
        FAVORITES.add(movie_id)
    print(FAVORITES)
    flash(f"Film {movie['title']} został dodany do ulubionych")
    return redirect(url_for('homepage'))


@app.route('/tv_series')
def tv_series():
    today = datetime.date.today()
    tv_series = get_tv_series()
    print(url_for('tv_series'))
    print(url_for(request.endpoint))
    return render_template("tv_series.html", tv_series=tv_series, movies_types_of_lists=movies_types_of_lists, today=today,
                           current_list=url_for(request.endpoint))


@app.route('/search')
def search():
    search_query = request.args.get("searched_phrase", "")
    if search_query:
        movies = searcher(search_query)
    else:
        movies =[]
    return render_template("search.html", movies=movies, search_query = search_query)


@app.context_processor
def utility_procesor():
    def tmdb_img_url(path, size):
        return get_poster(path, size)
    return {"tmdb_img_url": tmdb_img_url}





if __name__ == '__main__':
    app.run(debug=True)

