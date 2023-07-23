import os
import sys
import webbrowser
# Appending the root directory of this project to the sys.path so that it can call
# other packages
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
sys.path.append(ROOT_DIR)

from movie_database_app.data import json_data_loader


def convert_html_template_to_string():
    """
    parse the html template file and convert it to a python string for later manipulation
    :return:html template as a string
    """
    html_template_file = os.path.join('website_generator', 'html_template.html')
    with open(html_template_file) as fileobj:
        html_string = fileobj.read()
        return html_string


def create_website_title():
    """
    stores html string in a variable and replaces the html title with another name
    :return:new html string with updated title
    """
    html_template = convert_html_template_to_string()
    new_html_template = html_template.replace('__TEMPLATE_TITLE__', 'Movie Database App')
    return new_html_template


def create_html_output_for_movie():
    """
    creates an html string that that includes all the html for the movies currently in
    the movie database file
    :return: movie database html string
    """
    movie_database_object = json_data_loader.load_json_movie_data()
    html_output = ''
    for movie in movie_database_object:
        html_output += '\n<li>\n<div class = "movie">\n'
        for movie_name, movie_info in movie.items():
            movie_img = movie_info['poster url']
            movie_name = movie_name
            movie_year = movie_info['year']
            html_output += f'<img class = "movie-poster" src = "{movie_img}" title>\n'
            html_output += f'<div class = "movie-title">{movie_name}</div>\n'
            html_output += f'<div class = "movie-year">{movie_year}</div>\n'
            html_output += '</div>\n'
            html_output += '</li>'
    return html_output


def generate_website_html():
    """
    creates a new file that stores the updates html from the html template file
    :return:
    """
    movie_database_html_file = os.path.join('website_generator', 'movie_database.html')
    html_template = create_website_title()
    html_movie_output = create_html_output_for_movie()
    latest_html_template = html_template.replace('__TEMPLATE_MOVIE_GRID__', html_movie_output)
    with open(movie_database_html_file, 'w') as fileobj:
        fileobj.write(latest_html_template)


def open_html():
    """
    opens the html file for the updated movie site
    :return:
    """
    webbrowser.open(os.path.join('website_generator', 'movie_database.html'))
    print('\nWebsite Generated!')


