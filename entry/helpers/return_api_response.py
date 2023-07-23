import requests

import json

OMDP_API_URL = 'http://www.omdbapi.com/?apikey=66544728&t='


def return_api_response_object():
    """
    gets user input to retrieve a string that is then appended to the movie database api
    url to search for a movie. Returns none if unable to connect, or if movie not found
    so that the function calling this function knows what to do with the response
    :return:json response object
    """
    movie_to_search = input('\nWhat is the name of the movie you would like to add: ')
    try:
        omdp_api_response = requests.get(OMDP_API_URL + movie_to_search)
    except requests.exceptions.ConnectionError:
        print('\nUnable to connect to the internet')
        return
    # Convert api json response object to a python object
    api_response_data_object = json.loads(omdp_api_response.text)
    if 'False' in api_response_data_object.values():
        return
    return api_response_data_object


# print(return_api_response_object())
