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

    def add(self, category):
        name = self.ui.get_user_input("Enter name: ")
        release_year = self.ui.get_valid_input("Enter release year: ", self.ui.validate_year)
        creator = self.ui.get_user_input("Enter creator: ")

        if category == 2:
            genre = self.ui.get_user_choice("Choose a genre:", self.music_genres)
            album = self.ui.get_user_input("Enter album: ")
            return Music(name, self.music_genres[genre], int(release_year), creator, album)

        elif category == 1:
            genre = self.ui.get_user_choice("Choose a genre:", self.genres)
            season = self.ui.get_valid_input("Enter season: ", self.ui.validate_positive_number)
            series = self.ui.get_valid_input("Enter series: ", self.ui.validate_positive_number)
            return TVShow(name, self.genres[genre], int(release_year), creator, int(season), int(series))

        else:
            genre = self.ui.get_user_choice("Choose a genre:", self.genres)
            return Movie(name, self.genres[genre], int(release_year), creator)

    def edit(self, category):
        items = self.catalog[category]
        if not items:
            self.ui.console_output_error("No items available in this category.")
            return

        item = self.ui.select_item_from_list(items, "Select an item to edit:")
        if not item:
            return

        self.ui.console_output(f"Editing '{item.name}':")
        item.name = self.ui.get_user_input("Enter new name: ") or item.name
        item.genre = self.ui.get_user_input("Enter new genre: ") or item.genre
        item.release_year = self.ui.get_valid_input("Enter release year: ", self.ui.validate_year) or item.release_year
        item.creator = self.ui.get_user_input("Enter new creator: ") or item.creator

        if isinstance(item, TVShow):
            item.season = int(self.ui.get_user_input("Enter new season: ") or item.season)
            item.series = int(self.ui.get_user_input("Enter new series: ") or item.series)
        elif isinstance(item, Music):
            item.album = self.ui.get_user_input("Enter new album: ") or item.album

        self.ui.console_output("Item updated successfully.")

    def remove(self, category):
        items = self.catalog[category]
        if not items:
            self.ui.console_output_error("No items available in this category.")
            return

        item = self.ui.select_item_from_list(items, "Select an item to remove:")
        if not item:
            return

        confirmation = self.ui.get_user_input(f"Are you sure you want to delete '{item.name}'? (y/n): ").lower()
        if confirmation == 'y':
            items.remove(item)
            self.ui.console_output("Item removed successfully.")

    def search(self, category, attribute, search_value):
        attribute_name = ATTRIBUTE_MAP.get(attribute)
        if not attribute_name:
            raise ValueError("Invalid attribute choice")

        found_items = [item for item in self.catalog[category]
                       if str(getattr(item, attribute_name, "")).lower() == search_value.lower()]

        return found_items

    def display(self):
        for i, category_items in enumerate(self.catalog):
            self.ui.console_output(f"\n{self.categories[i + 1]}:")
            for item in category_items:
                self.ui.console_output(str(item))
