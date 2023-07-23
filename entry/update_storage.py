import json
import os
import data_loader
from helpers import return_api_response


def list_movies_in_database(filepath):
    """
    access current json movie data and print out each one along with its info
    :return:
    """
    movie_database_object = data_loader.load_json_movie_data(filepath)
    print(f"\ntotal movies: {len(movie_database_object)}")
    for movie in movie_database_object:
        for movie_name, movie_info in movie.items():
            print(f'\n{movie_name}:\n')
            for movie_info_category, movie_info_details in movie_info.items():
                print(f'{movie_info_category}: {movie_info_details}')


def add_movie_info(filename):
    """
    store python representation of json api data in a variable and attempts to initialize
    variables which hold dictionary key value pairs representing specific movie data. Either
    appends movie info dictionary to json database or handles it based on api response
    :return:
    """

    movie_database_object = data_loader.load_json_movie_data(filename)
    api_response_object = return_api_response.return_api_response_object()
    json_movie_database_file = os.path.join('data', 'movie_database_file.json')
    print(json_movie_database_file)
    try:
        movie_title = api_response_object['Title']
    except TypeError:
        print('\nMovie not available to add')
        return
    movie_rating = float(api_response_object['imdbRating'])
    movie_year = int(api_response_object['Year'])
    movie_poster_url = api_response_object['Poster']
    for movie in movie_database_object:
        if movie_title in movie:
            print('\nmovie already exists in database\nPlease select option 4 to change movie info')
            return
    new_movie_dictionary = {
        movie_title: {
            'rating': movie_rating,
            'year': movie_year,
            'poster url': movie_poster_url
        }
    }
    movie_database_object.append(new_movie_dictionary)
    with open(json_movie_database_file, 'w') as fileobj:
        json.dump(movie_database_object, fileobj, indent=4)


def delete_movie_from_database(filename):
    """
    uses enumerate function to be able to delete movie based on index position if movie
    found in database
    :return:
    """
    movie_database_object = data_loader.load_json_movie_data(filename)
    json_movie_database_file = os.path.join('data', 'movie_database_file.json')
    movie_to_delete = input("\nWhich movie would you like to remove from the database: ").title()
    for index, movie in enumerate(movie_database_object):
        if movie_to_delete in movie:
            del movie_database_object[index]
            with open(json_movie_database_file, 'w') as fileobj:
                json.dump(movie_database_object, fileobj, indent=4)
            print("\nMovie deleted from database!")
            return
    print("\nMovie not found in database")


def update_movie_rating(filename):
    movie_database_object = data_loader.load_json_movie_data(filename)
    json_movie_database_file = os.path.join('data', 'movie_database_file.json')
    movie_to_update = input("\nWhich movie would you like to update: ").title()
    if movie_to_update.isspace() or not movie_to_update:
        print('\nPlease do not enter an empty field')
        return
    try:
        movie_rating_update = float(input("\nre-rate the movie: "))
    except ValueError:
        print('\nPlease enter a valid movie rating using numbers only')
        return
    for movie in movie_database_object:
        for movie_name, movie_info in movie.items():
            if movie_to_update in movie_name:
                movie_info['rating'] = movie_rating_update
                print(f"\n{movie_to_update} is now rated {movie_rating_update}!")
                with open(json_movie_database_file, 'w') as fileobj:
                    json.dump(movie_database_object, fileobj, indent=4)
                return
    print("\nMovie not found in database")
