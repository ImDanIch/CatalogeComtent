from datetime import datetime
from user_interface import UserInterface
from catalog import Music, Movie, TVShow
from options_data import ATTRIBUTE_MAP


class CatalogManager:
    def __init__(self, catalog, categories, genres, music_genres):
        self.catalog = catalog
        self.categories = categories
        self.genres = genres
        self.music_genres = music_genres
        self.ui = UserInterface()

    def validate_year(self, value, current_year):
        if value.isdigit():
            year = int(value)
            return 1400 <= year <= current_year
        return False

    def validate_positive_number(self, value):
        return value.isdigit() and int(value) > 0

    def get_valid_input(self, prompt, validation_function, error_message, *args):
        while True:
            value = self.ui.handle_user_interaction('input', prompt)
            if validation_function(value, *args):
                return value
            self.ui.handle_user_interaction('error', error_message)

    def select_item_from_list(self, items, prompt):
        if not items:
            self.ui.handle_user_interaction('output', "No items available.")
            return None

        self.ui.handle_user_interaction('output', prompt)
        for i, item in enumerate(items, start=1):
            self.ui.handle_user_interaction('output', f"{i}: {item.name}")  # Выводим название элемента

        while True:
            try:
                choice = int(self.ui.handle_user_interaction('input', "Enter the number of the item or 0 to go back: "))
                if choice == 0:
                    return None
                if 1 <= choice <= len(items):
                    return items[choice - 1]
                else:
                    self.ui.handle_user_interaction('error', "Invalid number. Please try again.")
            except ValueError:
                self.ui.handle_user_interaction('error', "Input must be a number. Please try again.")

    def add_content(self, category):
        current_year = datetime.now().year
        category_name = self.categories[category]

        name = self.ui.handle_user_interaction('input', f"Enter {category_name} name: ")
        release_year = self.get_valid_input(
            "Enter release year: ", self.validate_year,
            f"Release year must be a number between 1400 and {current_year}.",
            current_year
        )
        creator = self.ui.handle_user_interaction('input', "Enter creator: ")

        if category_name == "Music":
            genre = self.music_genres.get(self.ui.handle_user_interaction('choice', "Choose a genre:", self.music_genres))
            album = self.ui.handle_user_interaction('input', "Enter album: ")
            return Music(name, genre, int(release_year), creator, album)

        elif category_name == "TV show":
            genre = self.genres.get(self.ui.handle_user_interaction('choice', "Choose a genre:", self.genres))
            season = self.get_valid_input(
                "Enter season: ", self.validate_positive_number,
                "Season must be a positive number."
            )
            series = self.get_valid_input(
                "Enter series: ", self.validate_positive_number,
                "Series must be a positive number."
            )
            return TVShow(name, genre, int(release_year), creator, int(season), int(series))

        else:  # For Movies
            genre = self.genres.get(self.ui.handle_user_interaction('choice', "Choose a genre:", self.genres))
            return Movie(name, genre, int(release_year), creator)

    def edit_content(self, category):
        category -= 1
        category_name = self.categories[category+1]
        items = self.catalog[category]

        if not items:
            self.ui.handle_user_interaction('output', f"No items available in {category_name}.")
            return

        item = self.select_item_from_list(items, f"Select an item to edit from {category_name}:")
        if not item:
            return

        self.ui.handle_user_interaction('output', f"Editing '{item.name}':")
        item.name = self.ui.handle_user_interaction('input', "Enter new name: ") or item.name
        item.genre = self.ui.handle_user_interaction('input', "Enter new genre: ") or item.genre
        item.release_year = int(self.ui.handle_user_interaction('input', "Enter new release year: ") or item.release_year)
        item.creator = self.ui.handle_user_interaction('input', "Enter new creator: ") or item.creator

        if isinstance(item, TVShow):
            item.season = int(self.ui.handle_user_interaction('input', "Enter new season: ") or item.season)
            item.series = int(self.ui.handle_user_interaction('input', "Enter new series: ") or item.series)
        elif isinstance(item, Music):
            item.album = self.ui.handle_user_interaction('input', "Enter new album: ") or item.album

        self.ui.handle_user_interaction('output', "Item updated successfully.")

    def remove_content(self, category):
        category -= 1
        category_name = self.categories[category+1]
        items = self.catalog[category]
        item = self.select_item_from_list(items, f"Select an item to remove from {category_name}:")

        if not item:
            return False

        confirmation = self.ui.handle_user_interaction('input',
                                                      f"Are you sure you want to delete '{item.name}'? (y/n): ").lower()
        if confirmation == 'y':
            self.catalog[category].remove(item)
            self.ui.handle_user_interaction('output', "Item removed successfully.")
            return True
        else:
            self.ui.handle_user_interaction('output', "Deletion canceled.")
            return False

    def search_content(self, category, attribute, search_value):
        attribute_name = ATTRIBUTE_MAP.get(attribute)
        category -= 1

        if not attribute_name:
            raise ValueError("Invalid attribute choice")

        category_list = self.catalog[category]
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

    def display_catalog(self):
        self.ui.handle_user_interaction('output', "\nMovies:")
        for movie in self.catalog[0]:
            self.ui.handle_user_interaction('output', str(movie))

        self.ui.handle_user_interaction('output', "\nTV Shows:")
        for tv_show in self.catalog[1]:
            self.ui.handle_user_interaction('output', str(tv_show))

        self.ui.handle_user_interaction('output', "\nMusic:")
        for music_item in self.catalog[2]:
            self.ui.handle_user_interaction('output', str(music_item))
