def main():
    """
    creates listener loop that only break when user enters 0 as an input, else runs the
    appropriate function
    :return:
    """

    print("Welcome to your Movie Database!")

    while True:
        user = input('Which file do you want to open')
        action_to_perform = display_menu_page()
        if action_to_perform == 1:
            update_movie_data.list_movies_in_database()
            return_to_menu_page()
        elif action_to_perform == 2:
            update_movie_data.add_movie_info()
            return_to_menu_page()
        elif action_to_perform == 3:
            update_movie_data.delete_movie_from_database()
            return_to_menu_page()
        elif action_to_perform == 4:
            update_movie_data.update_movie_rating()
            return_to_menu_page()
        elif action_to_perform == 5:
            print_average_movie_rating()
            print_median_movie_rating()
            print_highest_rated_movie()
            print_lowest_rated_movie()
            return_to_menu_page()
        elif action_to_perform == 6:
            print_random_movie()
            return_to_menu_page()
        elif action_to_perform == 7:
            return_movie_from_database()
            return_to_menu_page()
        elif action_to_perform == 8:
            return_ranked_list_of_movies()
            return_to_menu_page()
        elif action_to_perform == 9:
            generate_website.generate_website_html()
            generate_website.open_html()
            return_to_menu_page()
        elif action_to_perform == 0:
            print('\nbye!')
            break


if __name__ == '__main__':
    main()