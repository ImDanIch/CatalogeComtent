from datetime import datetime
from user_interface import UserInterface
from catalog import Music, Movie, TVShow

ui = UserInterface()


def add_content(category, categories, genres, music_genres):
    current_year = datetime.now().year
    category_name = categories[category]

    name = input(f"Enter {category_name} name: ")
    while True:
        try:
            release_year = int(input(f"Enter release year: "))
            if 1400 <= release_year <= current_year:
                break
            else:
                print(f"\nError: Invalid release year. Please try again.\n")
        except ValueError:
            print(f"\nError: Release year must be a number. Please try again.\n")

    creator = input("Enter creator: ")

    if category_name == "Music":
        genre = music_genres.get(ui.choose_option(music_genres, "genre"))
        album = input("Enter album: ")
        return Music(name, genre, release_year, creator, album)
    elif category_name == "TV show":
        genre = genres.get(ui.choose_option(genres, "genre"))
        season = int(input("Enter season: "))
        series = int(input("Enter series: "))
        return TVShow(name, genre, release_year, creator, season, series)
    else:
        genre = genres.get(ui.choose_option(genres, "genre"))
        return Movie(name, genre, release_year, creator)


def remove_content(catalog, category, categories):
    category_list = catalog[category]
    category_name = categories[category]

    if not category_list:
        print(f"\nNo items available in {category_name}.\n")
        return False

    print("\nSelect an item to remove:")
    for i, item in enumerate(category_list, start=1):
        print(f"{i}: {item}")

    try:
        item_num = int(input("Enter the item number to remove or 0 to go back: "))
        if item_num == 0:
            return False
        elif 1 <= item_num <= len(category_list):
            confirmation = input(f"Are you sure you want to delete '{category_list[item_num - 1]}'? (y/n): ").lower()
            if confirmation == 'y':
                category_list.pop(item_num - 1)
                return True
            else:
                print("Deletion canceled.")
                return False
        else:
            print("Invalid item number.")
            return False
    except ValueError:
        print("Invalid input.")
        return False


def search_content(catalog, category, attribute, search_value):
    category_list = catalog[category]

    found_items = []
    for item in category_list:
        item_attribute_value = getattr(item, attribute.lower(), "").lower()
        if item_attribute_value == search_value.lower():
            found_items.append(item)

    return found_items


def display_catalog(catalog):
    print("\nMovies:")
    for movie in catalog[0]:
        print(movie)

    print("\nTV Shows:")
    for tv_show in catalog[1]:
        print(tv_show)

    print("\nMusic:")
    for music_item in catalog[2]:
        print(music_item)
