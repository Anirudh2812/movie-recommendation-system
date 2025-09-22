import sqlite3
from tabulate import tabulate

DB_NAME = "movies.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def get_movies_by_rating(min_rating):
    conn = connect_db()
    cur = conn.cursor()
    query = """
    SELECT m.title, ROUND(AVG(r.rating),2) as avg_rating, COUNT(r.rating) as num_ratings
    FROM movies m
    JOIN ratings r ON m.movieId = r.movieId
    GROUP BY m.movieId
    HAVING avg_rating >= ?
    ORDER BY avg_rating DESC
    LIMIT 50;
    """
    cur.execute(query, (min_rating,))
    results = cur.fetchall()
    conn.close()
    return results

def main():
    print("🎬 Welcome to Movie Recommendation System 🎬")
    print("Select rating category:")
    print("4 4 stars and above")
    print("3 3 stars and above")
    print("2 2 stars and above")
    print("1 1 star and above")
    
    choice = input("Enter choice (1-4): ")
    rating_map = {"1": 1, "2": 2, "3": 3, "4": 4}
    
    if choice not in rating_map:
        print("Invalid choice 😢")
        return
    
    min_rating = rating_map[choice]
    movies = get_movies_by_rating(min_rating)
    
    if movies:
        print(f"\nMovies with rating >= {min_rating} ⭐:\n")
        print(tabulate(movies, headers=["Title", "Avg Rating", "Num Ratings"], tablefmt="fancy_grid"))
    else:
        print("No movies found 😢")

if __name__ == "__main__":
    main()
1
