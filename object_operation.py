from datetime import datetime
from user_interface import UserInterface
from catalog import Music, Movie, TVShow

ui = UserInterface()


def validate_year(value, current_year):
    if value.isdigit():
        year = int(value)
        return 1400 <= year <= current_year
    return False


def validate_positive_number(value):
    return value.isdigit() and int(value) > 0


def select_item_from_list(items, prompt):
    if not items:
        ui.handle_user_interaction('output', "No items available.")
        return None

    ui.handle_user_interaction('output', prompt)
    for i, item in enumerate(items, start=1):
        ui.handle_user_interaction('output', f"{i}: {item.name}")  # Выводим название элемента

    while True:
        try:
            choice = int(ui.handle_user_interaction('input', "Enter the number of the item or 0 to go back: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                ui.handle_user_interaction('error', "Invalid number. Please try again.")
        except ValueError:
            ui.handle_user_interaction('error', "Input must be a number. Please try again.")


def get_valid_input(prompt, validation_function, error_message, *args):
    while True:
        value = ui.handle_user_interaction('input', prompt)
        if validation_function(value, *args):
            return value
        ui.handle_user_interaction('error', error_message)


def add_content(category, categories, genres, music_genres):
    current_year = datetime.now().year
    category_name = categories[category]

    name = ui.handle_user_interaction('input', f"Enter {category_name} name: ")
    release_year = get_valid_input(
        "Enter release year: ", validate_year,
        f"Release year must be a number between 1400 and {current_year}.",
        current_year
    )
    creator = ui.handle_user_interaction('input', "Enter creator: ")

    if category_name == "Music":
        genre = music_genres.get(ui.handle_user_interaction('choice', "Choose a genre:", music_genres))
        album = ui.handle_user_interaction('input', "Enter album: ")
        return Music(name, genre, int(release_year), creator, album)

    elif category_name == "TV show":
        genre = genres.get(ui.handle_user_interaction('choice', "Choose a genre:", genres))
        season = get_valid_input(
            "Enter season: ", validate_positive_number,
            "Season must be a positive number."
        )
        series = get_valid_input(
            "Enter series: ", validate_positive_number,
            "Series must be a positive number."
        )
        return TVShow(name, genre, int(release_year), creator, int(season), int(series))

    else:  # For Movies
        genre = genres.get(ui.handle_user_interaction('choice', "Choose a genre:", genres))
        return Movie(name, genre, int(release_year), creator)


def edit_content(catalog, category, categories):
    category -= 1
    category_name = categories[category+1]
    items = catalog[category]

    if not items:
        ui.handle_user_interaction('output', f"No items available in {category_name}.")
        return

    item = select_item_from_list(items, f"Select an item to edit from {category_name}:")
    if not item:
        return

    ui.handle_user_interaction('output', f"Editing '{item.name}':")
    item.name = ui.handle_user_interaction('input', "Enter new name: ") or item.name
    item.genre = ui.handle_user_interaction('input', "Enter new genre: ") or item.genre
    item.release_year = int(ui.handle_user_interaction('input', "Enter new release year: ") or item.release_year)
    item.creator = ui.handle_user_interaction('input', "Enter new creator: ") or item.creator

    if isinstance(item, TVShow):
        item.season = int(ui.handle_user_interaction('input', "Enter new season: ") or item.season)
        item.series = int(ui.handle_user_interaction('input', "Enter new series: ") or item.series)
    elif isinstance(item, Music):
        item.album = ui.handle_user_interaction('input', "Enter new album: ") or item.album

    ui.handle_user_interaction('output', "Item updated successfully.")


def remove_content(catalog, category, categories):
    category -= 1
    category_name = categories[category+1]
    items = catalog[category]
    item = select_item_from_list(items, f"Select an item to remove from {category_name}:")

    if not item:
        return False

    confirmation = ui.handle_user_interaction('input',
                                              f"Are you sure you want to delete '{item.name}'? (y/n): ").lower()
    if confirmation == 'y':
        catalog[category].remove(item)
        ui.handle_user_interaction('output', "Item removed successfully.")
        return True
    else:
        ui.handle_user_interaction('output', "Deletion canceled.")
        return False


ATTRIBUTE_MAP = {
    1: 'name',
    2: 'genre',
    3: 'release_year',
    4: 'creator'
}


def search_content(catalog, category, attribute, search_value):
    attribute_name = ATTRIBUTE_MAP.get(attribute)
    category -= 1

    if not attribute_name:
        raise ValueError("Invalid attribute choice")

    category_list = catalog[category]
    found_items = []

    search_value = str(search_value).lower()

    for item in category_list:
        if not hasattr(item, attribute_name):
            continue

        item_attribute_value = getattr(item, attribute_name, None)

        if item_attribute_value is not None:
            if isinstance(item_attribute_value, str):
                item_attribute_value = item_attribute_value.lower()

            if item_attribute_value == search_value:
                found_items.append(item)

    return found_items


def display_catalog(catalog):
    ui.handle_user_interaction('output', "\nMovies:")
    for movie in catalog[0]:
        ui.handle_user_interaction('output', str(movie))

    ui.handle_user_interaction('output', "\nTV Shows:")
    for tv_show in catalog[1]:
        ui.handle_user_interaction('output', str(tv_show))

    ui.handle_user_interaction('output', "\nMusic:")
    for music_item in catalog[2]:
        ui.handle_user_interaction('output', str(music_item))
