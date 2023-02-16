# Lesson SE-T38
# Task 2


# watch_next.py--a program that recommends a movie that is similar to
#   the description of the film that has been watched previously.
#   In our example "Planet Hulk".


# Import NLP module
import spacy

# Load language module.
nlp = spacy.load('en_core_web_md')

# Define a function that returns the most similar movie.
def most_similarMovie(description, movie_list):
    description = nlp(description)
    watch_next = []
    similarity_degree = []

    for movie in movie_list:
        token = nlp(movie)
        movie = movie.strip(":")
        watch_next += [[movie[:7], movie[9:], token.similarity(description)]]
        similarity_degree += [token.similarity(description)]

    # Find the movie with the highest similarity and display title and description.
    for watch in watch_next:
        if max(similarity_degree) == watch[2]:
            print("\n  Title:", watch[0], "\n")
            print("  Description:\n")
            print(" ",watch[1][:100])
            print(" ",watch[1][100:200])
            print(" ",watch[1][200:300])
            print(" ",watch[1][300:400])
            print(" ",watch[1][400:500])
    print()

# Create a list of movies.
movie_list = []

# Read the movies text file and store in the movie list.
# If the text file is non existing display a message to the user.
try:
    with open("movies.txt", "r") as movies:
        for movie in movies:
            movie = movie.strip("\n")
            movie_list += [movie]

except FileNotFoundError:
    print("\n\t\t***Movie file \"movies.txt\" does not exist***")
    print("\n\tPlease add or check movies.txt file and run the program again!\n")
    exit()

# A description of a movie, in this case "Planet Hulk".
description = """
    Will he save their world or destroy it? When the hulk becomes too 
    dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into 
    space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet
    Sakaar where he is sold into slavery and trained as a gladiator.
                                                                                            """

# Call the most_similarMovie function which returns the title and a description of 
#   the movie from the text file most similar to the previously watched movie.
print("\n  If you liked \"Planet Hulk\" you may enjoy the following movie:")
most_similarMovie(description, movie_list)
