import json
import os
# Any manipulating of data can be done from the object returned by these function


def load_json_movie_data(filename):
    """
    open json file and return python object representation
    :param filename: name of file to open
    :return:
    """
    # create os independent file path to check file names
    user_json_file = os.path.join('data', filename + '.json')
    with open(user_json_file, 'r') as fileobj:
        python_data_object = json.load(fileobj)
        return python_data_object


def dump_json_movie_data(filename, json_object_equivalent):
    """
    takes a python object that can be converted into a json object and writes it to a json file.
    Creates the file if the filename does not exist.
    :param filename:
    :param json_object_equivalent:
    :return:
    """
    # create os independent file path to check file names
    user_json_file = os.path.join('data', filename + '.json')
    with open(user_json_file, 'w') as filobj:
        json.dump(json_object_equivalent, filobj)
