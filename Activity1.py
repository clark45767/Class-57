import sqlite3
import pandas as pd

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.executescript("""
drop table if exists movie;
drop table if exists actor;
drop table if exists movie_actor;

create table movie (
    movie_id   integer primary key,
    title       text,
    genre       text,
    year        integer,
    rating      real,
    duration    integer
);

create table actor (
    actor_id      integer primary key,
    actor_name    text,
    birth_year    integer,
    country       text
);


create table movie_actor (
    movie_id     integer,
    actor_id     integer
);

insert into movie values
    (1,'The Lion King','Animation',1994,8.5,88),
    (2,'Toy Story','Animation',1995,8.3,81),
    (3,'Frozen','Animation',2013,7.4,102),
    (4,'Moana','Animation',2016,7.6,107),
    (5,'Spider-Man','Action',2002,7.3,121),
    (6,'Black Panther','Action',2018,7.3,134),
    (7,'Avegners','Action',2012,8.0,143),
    (8,'Matilda','Drama',1996,7.0,98),
    (9,'Home Alone','Comedy',1990,7.7,103),
    (10,'Elf','Comedy',2003,6.9,97),
    (11,'Coco','Animation',2017,8.4,88),
    (12,'Intestellar','Drama',2014,8.6,169);


INSERT INTO Actor VALUES
    (1,'Tom Hanks',1956,'USA'),
    (2,'Idris Elba',1972,'UK'),
    (3,'Chadwick Boseman',1976'USA'),
    (4,'Scarlett Johansson',1984,'USA'),
    (5,'Macaulay Culkin',1980,'USA'),
    (6,'Will Smith',1968,'USA'),
    (7,'Meryl Streep',1949,'USA'),
    (8,'Lupita Nyongo',1983,'Kenya'),
    (9,'Priyanka Chopra',1982,'India'),
    (10,'Jackie Chan',1954,'China');

INSERT INTO Movie_Actor VALUES
    (1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);
""")
conn.commit()
print('Database ready!')


#Part 2

genres = pd.read_sql("""select distinct(genre)
    from movie;""", conn)
print(genres)

countries = pd.read_sql("""select distinct(country)
    from actor;""", conn)
print(countries)


#part 3
top_movies = pd.read_sql("""select title, genre, rating
    from movie
    order byr ating DESC;""",conn)
print(top_movies)


