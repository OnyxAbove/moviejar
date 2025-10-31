import random
import os

class Jar:
    def __init__(self, filename="~/Documents/moviejar.txt"):
        self.file_path = os.path.expanduser(filename)
        # Create file if it doesn't exist
        if not os.path.exists(self.file_path):
            open(self.file_path, 'a').close()

    def pickrand(self, rating=None, genre=None, mode=None):
        with open(self.file_path, "r") as file:
            movielist = [line.strip().split(", ") for line in file if line.strip()]

        if not movielist:
            return "No movies in jar!"

        # Filter by rating
        if rating:
            movielist = [movie for movie in movielist if len(movie) > 1 and movie[1] == rating.upper()]

        # Filter by genre
        if genre:
            movielist = [movie for movie in movielist if len(movie) > 2 and movie[2].upper() == genre.upper()]

        if not movielist:
            return "No movies match your criteria!"

        # Pick random movie
        movie = random.choice(movielist)

        # Remove from file if mode is 'd' (destructive)
        if mode == "d":
            self._remove_movie_from_file(movie)

        return movie[0]

    def _remove_from_file(self, movie_to_remove):
        """Helper method to remove a movie from the file"""
        with open(self.file_path, "r") as file:
            lines = file.readlines()

        movie_str = ", ".join(movie_to_remove)
        with open(self.file_path, "w") as file:
            for line in lines:
                if line.strip() != movie_str:
                    file.write(line)

    def clear(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            # Recreate empty file
            open(self.file_path, 'a').close()
            print("Jar cleared.")

    def list(self):  # Added 'self' parameter
        if not os.path.exists(self.file_path):
            print("No movies in jar!")
            return

        with open(self.file_path, "r") as file:
            content = file.read().strip()
            if content:
                print(content)
            else:
                print("No movies in jar!")

    def remove(self, name: str):
        if not os.path.exists(self.file_path):
            print("No movies in jar!")
            return

        with open(self.file_path, "r") as file:
            lines = file.readlines()

        found = False
        with open(self.file_path, "w") as file:
            for line in lines:
                if not line.strip().startswith(name):
                    file.write(line)
                else:
                    found = True

        if found:
            print(f"Removed '{name}' from jar")
        else:
            print(f"Movie '{name}' not found in jar")

    def new(self):
        movie = []
        movie.append(input("Enter the name of the movie: "))

        ratings = ["G", "PG", "PG-13", "R", "X"]
        rating = input("Enter the Rating [G, PG, PG-13, R, X]: ")
        while rating.upper() not in ratings:
            rating = input("Enter the Rating [G, PG, PG-13, R, X]: ")
        movie.append(rating.upper())

        genres = ["ACTION", "COMEDY", "DRAMA", "HORROR", "SCIENCE FICTION", "SCI-FI", 
                  "ROMANCE", "ROMCOM", "ADVENTURE", "THRILLER", "MYSTERY", "CRIME", "FANTASY"]
        genre = input("Enter the genre of the movie ('?' for options): ")
        while genre.upper() not in genres:
            if genre == "?":
                print("Your options are: ACTION, COMEDY, DRAMA, HORROR, SCIENCE FICTION, SCI-FI, ROMANCE, ROMCOM, ADVENTURE, THRILLER, MYSTERY, CRIME, FANTASY")
                genre = input("Enter the genre of the movie: ")
            else: 
                print("Invalid Option")
                genre = input("Enter the genre of the movie ('?' for options): ")
        movie.append(genre.upper())  # Now storing as uppercase

        with open(self.file_path, "a") as file:
            file.write(", ".join(movie) + "\n")

        print(f"Added '{movie[0]}' to jar!")

