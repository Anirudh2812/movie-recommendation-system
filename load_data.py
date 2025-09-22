import pandas as pd 
import sqlite3

#Connection to the database 
conn = sqlite3.connect("movies.db")

#Loading CSV files 
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")

#Write to SQLite
try:
    movies.to_sql("movies", conn, if_exists = "replace", index = False)
    ratings.to_sql("ratings", conn, if_exists = "replace", index = False)
    tags.to_sql("tags", conn, if_exists = "replace", index = False)
    links.to_sql("links", conn, if_exists = "replace", index = False)

    conn.close()
    print("All CSVs loaded into movies.db successfully")

except Exception as e:
    print(e)