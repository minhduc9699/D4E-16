import pymysql

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

movie_id = '1211'
movie_name = 'tenet'
movie_year = '2020'
writer = 'CN'
movie_actor = []

cursor.execute(f''' 
    INSERT INTO d4e16.movie(id, title, year, writer)
    VALUES ('{movie_id}', '{movie_name}', '{movie_year}', '{writer}')
''')

client.commit()