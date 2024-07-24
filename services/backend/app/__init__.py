from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config.from_object('app.config.Config')
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)


class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    age_rating = db.Column(db.Integer)
    countries = db.Column(db.String)
    poster = db.Column(db.String)
    description = db.Column(db.String)
    short_description = db.Column(db.String)
    movie_length = db.Column(db.Integer)
    is_series = db.Column(db.Boolean)
    series_length = db.Column(db.Integer)

    def __init__(self, id: int, name: str, genres: str, year: int, rating: int, age_rating: int, countries: str,
                 poster: str, description: str, short_description: str, movie_length: int, is_series: bool,
                 series_length: int):
        self.id = id
        self.name = name
        self.genres = genres
        self.year = year
        self.rating = rating
        self.age_rating = age_rating
        self.countries = countries
        self.poster = poster
        self.description = description
        self.short_description = short_description
        self.movie_length = movie_length
        self.is_series = is_series
        self.series_length = series_length


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    photo = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)

    def __init__(self, id: int, name: str, photo: str, gender: str, age: int):
        self.id = id
        self.name = name
        self.photo = photo
        self.gender = gender
        self.age = age


class FilmActor(db.Model):
    __tablename__ = 'films_actors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))

    def __init__(self, actor_id: int, film_id: int):
        self.actor_id = actor_id
        self.film_id = film_id


@app.route("/")
def hello_world():
    return {'hello': 'world'}
