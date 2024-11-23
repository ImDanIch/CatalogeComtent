import json
from catalog import Movie, TVShow, Music


def save_data(catalog):
    data = {
        'movies': [],
        'tv_shows': [],
        'music': [],
    }

    for movie in catalog[0]:
        movie_dict = movie.to_dict()
        data['movies'].append(movie_dict)

    for tv_show in catalog[1]:
        tv_show_dict = tv_show.to_dict()
        data['tv_shows'].append(tv_show_dict)

    for music_item in catalog[2]:
        music_dict = music_item.to_dict()
        data['music'].append(music_dict)

    with open('catalog_data.json', 'w') as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open('catalog_data.json', 'r') as file:
            data = json.load(file)

        movies = [Movie(**item) for item in data.get('movies', [])]
        tv_shows = [TVShow(**item) for item in data.get('tv_shows', [])]
        music = [Music(**item) for item in data.get('music', [])]

        return movies, tv_shows, music

    except FileNotFoundError:
        return [], [], []