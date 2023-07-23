import random as rand

import data_loader


def return_to_menu_page():
    confirm_return_to_menu = input("\nPress enter to return to the main page")


def display_menu_page():
    """
    if user enters anything other than valid input, listener loop will continue to list menu
    selection and will only ever return valid input allowing for the main loop to always run
    unless the exit input (0) is entered
    :return: only return valid user input so that the program does not break
    """

    valid_inputs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    is_valid_action = False

    while not is_valid_action:
        print("""
0. Exit app

1. List movies

2. Add movie

3. Delete movie

4. Update movie

5. Movie stats

6. Select random movie

7. Search movie

8. Sort movies by rating

9. Generate website""")

        print("\nPlease enter a valid menu selection to perform")
        action_to_perform = input("\nWhich action would you like to perform (0-8): ")
        if action_to_perform in [" ", ""] or action_to_perform not in valid_inputs:
            continue
        else:
            return int(action_to_perform)


def return_sorted_dictionary_of_movie_ratings():
    """
    initializes a dictionary and adds new key value pairs to for each movie and its rating in
    the data file and then uses a lambda function to sort it by its values.
    :return:
    """
    movie_database_file = data_loader.load_json_movie_data()
    list_of_movie_ratings = {}
    for movie in movie_database_file:
        for movie_name, movie_info in movie.items():
            list_of_movie_ratings[movie_name] = movie_info['rating']
    sorted_list_of_movie_ratings = sorted(list_of_movie_ratings.items(), key=lambda kv: kv[1])
    return dict(sorted_list_of_movie_ratings)


def print_average_movie_rating():
    """
    sums a list of dictionary values and calculates their average
    :return:
    """
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    movie_ratings = []
    movies_in_database = 0
    for movie_rating in sorted_movie_ratings_dictionary.values():
        movies_in_database += 1
        movie_ratings.append(movie_rating)
    average_movie_ratings = sum(movie_ratings) / movies_in_database
    print(f"\nAverage movie rating is {round(average_movie_ratings, 2)}")


def print_median_movie_rating():
    """
    sorts a list of movie ratings and then prints out either middle one or middle two ratings
    :return:
    """
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    list_of_movie_ratings = []
    median_index_position = len(sorted_movie_ratings_dictionary) // 2
    for movie_rating in sorted_movie_ratings_dictionary.values():
        list_of_movie_ratings.append(movie_rating)
    sorted_list_of_movies = sorted(list_of_movie_ratings)
    if len(list_of_movie_ratings) % 2 == 1:
        print(f"\nMedian movie rating is {sorted_list_of_movies[median_index_position]}")
    else:
        print(f"\nMedian movie rating are "
              f"{sorted_list_of_movies[median_index_position - 1]} "
              f"and {sorted_list_of_movies[median_index_position]}")


def print_highest_rated_movie():
    """
    :return:
    """
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    highest_movie_rating = list(sorted_movie_ratings_dictionary.values())[-1]
    print('\nThe highest rated movies are:\n')
    for movie, rating in sorted_movie_ratings_dictionary.items():
        if rating == highest_movie_rating:
            print(f'{movie}: {rating}')


def print_lowest_rated_movie():
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    lowest_movie_rating = list(sorted_movie_ratings_dictionary.values())[0]
    print('\nThe lowest rated movies are:\n')
    for movie, rating in sorted_movie_ratings_dictionary.items():
        if rating == lowest_movie_rating:
            print(f'{movie}: {rating}')


def print_random_movie():
    """
    uses random module to select a random movie from a list converted from a dictionary
    :return:
    """
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    random_movie_selection = rand.choice(list(sorted_movie_ratings_dictionary.items()))
    movie = random_movie_selection[0]
    movie_rating = random_movie_selection[1]
    print(f"\nWould you like to watch {movie}? You've previously given it a rating of {movie_rating}")


def return_movie_from_database():
    """
    returns a movie from dictionary of movies and ratings based on user input
    :return:
    """
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    substring_to_check = input("\nEnter a part of the movie title you would like to look up: ")
    for movie, movie_rating in sorted_movie_ratings_dictionary.items():
        if substring_to_check.title() in movie:
            print(f'{movie} is rated {movie_rating}')


def return_ranked_list_of_movies():
    sorted_movie_ratings_dictionary = return_sorted_dictionary_of_movie_ratings()
    for movie, movie_rating in tuple(sorted_movie_ratings_dictionary.items())[::-1]:
        print('')
        print(f'{movie} is rated {movie_rating}')
