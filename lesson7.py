import sqlite3
import pandas as pd

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISYS Movie_Actor;


CREATE TABLE Movie(
    Movie_id  INTERGER PRIMARY KEY,
    Title     TEXT,
    Genre     TEXT,
    Year      INTERGER,
    Rating    REAL,
    Duration  INTERGER,
);

CREATE TABLE Actor (
    Actor_Id   INTERGER PRIMARY KEY,
    Actor_NAME TEXT,
    Birth_Year INTERGER,
    Country    TEXT
);

CREATE TABLE Movie VALUES
(1,'The lion king','Animation',1994,8.5,88)
(2,'Toy Story','Animation',1995,8.3,88)
(3,'Frozen','Animation',2013,7.4,88)
(4,'Moana','Animation',2016,7.6,88)
(5,'Spider-man','Action',2002,7.3,88)
(6,'Black Panther','Action',2018,7.3,88)
(7,'Avengers','Action',2012,8.0,39)
(8,'Matilda','Drama',1996,7.0,123)
(9,'Home Alone','Comedy',1990,7.7,48)
(10,'Elf','Comedy',2003,6.9,87)
(11,'Coco','Animation',2017,8.4,67)
(12,Interstellar','Drama',2014,8.6,169)

INSERT INTO Actor VALUES

(1,'Tom Hanks',1956,'USA'),

(2,'Idris Elba',1972,'UK'),

(3,'Chadwick Boseman',1976,'USA'),

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
genres = pd.read_sql("""SELECT DISTINCT(Genre)
s)
FROM Movie;""", conn)

print(genres)