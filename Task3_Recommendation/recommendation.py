import math

MOVIES = {
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Inception": ["Action", "Sci-Fi", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Godfather": ["Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama", "Thriller"],
    "The Avengers": ["Action", "Sci-Fi", "Adventure"],
    "Titanic": ["Drama", "Romance"],
    "The Notebook": ["Drama", "Romance"],
    "Toy Story": ["Animation", "Adventure", "Comedy"],
    "Finding Nemo": ["Animation", "Adventure", "Comedy"],
    "The Matrix": ["Action", "Sci-Fi"],
    "John Wick": ["Action", "Thriller"],
}


def build_genre_vector(movie_genres, all_genres):
    """Convert a list of genres into a binary vector based on all_genres order."""
    return [1 if genre in movie_genres else 0 for genre in all_genres]


def cosine_similarity(vec_a, vec_b):
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a * a for a in vec_a))
    magnitude_b = math.sqrt(sum(b * b for b in vec_b))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)


def get_all_genres(movies):
    genres = set()
    for genre_list in movies.values():
        genres.update(genre_list)
    return sorted(genres)


def recommend_movies(liked_movie, movies, top_n=3):
    if liked_movie not in movies:
        return None

    all_genres = get_all_genres(movies)
    liked_vector = build_genre_vector(movies[liked_movie], all_genres)

    scores = []
    for title, genres in movies.items():
        if title == liked_movie:
            continue
        movie_vector = build_genre_vector(genres, all_genres)
        similarity = cosine_similarity(liked_vector, movie_vector)
        scores.append((title, similarity))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


def main():
    print("=== Movie Recommendation System ===\n")
    print("Available movies:")
    for title in MOVIES:
        print(f"  - {title}")

    print()
    liked_movie = input("Enter a movie you like from the list above: ").strip()

    matched_title = None
    for title in MOVIES:
        if title.lower() == liked_movie.lower():
            matched_title = title
            break

    if not matched_title:
        print("Movie not found in our database. Please try again with an exact name.")
        return

    recommendations = recommend_movies(matched_title, MOVIES, top_n=3)

    print(f"\nBecause you liked '{matched_title}', you might also enjoy:")
    for title, score in recommendations:
        print(f"  - {title}  (similarity: {score:.2f})")


if __name__ == "__main__":
    main()