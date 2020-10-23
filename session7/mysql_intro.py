import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()

client = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='@gmail.com'
)

cursor = client.cursor()

# cursor.execute('CREATE DATABASE d4e16')
# cursor.execute('''
#     CREATE TABLE d4e16.movie(
#         id varchar(225) PRIMARY KEY,
#         title varchar(255),
#         year varchar(255),
#         writer varchar(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE d4e16.actor(
#         name varchar(255) PRIMARY KEY
#     )
# ''')
# cursor.execute(''' 
#     CREATE TABLE d4e16.`movie-actor`(
#         movie_id varchar(255),
#         actor_name varchar(255),
#         PRIMARY KEY(movie_id, actor_name),
#         FOREIGN KEY(movie_id) REFERENCES d4e16.movie(id),
#         FOREIGN KEY(actor_name) REFERENCES d4e16.actor(name)
#     )
# ''')

mongo_database = mongo_client.get_database('mongo_ex')
movie_collection = mongo_database.get_collection('movies')

movies = movie_collection.find({'actors': {'$ne': None}}) # EXTRACT

for movie in movies:
    cursor.execute(f''' 
        INSERT INTO d4e16.movie(id, title, year, writer)
        VALUES ('{movie["_id"]}', '{movie["title"]}', '{movie["year"]}', '{movie["writer"]}')
    ''')

client.commit()