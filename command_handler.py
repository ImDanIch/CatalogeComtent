from catalog_manager import CatalogManager
from file_manager import save_data


class CommandHandler:
    def __init__(self, catalog, ui, categories, genres, music_genres, attributes):
        self.catalog = catalog
        self.ui = ui
        self.categories = categories
        self.genres = genres
        self.music_genres = music_genres
        self.attributes = attributes
        self.catalog_manager = CatalogManager(self.catalog, self.categories, self.genres, self.music_genres)

    def execute_command(self, command):
        actions = {
            1: self.add_content,
            2: self.edit_content,
            3: self.remove_content,
            4: self.search_content,
            5: self.display_catalog,
            0: self.exit_program,
        }

        action = actions.get(command)
        if action:
            action()
        else:
            self.ui.console_output_error("\nInvalid command. Please try again.")

    def add_content(self):
        category = self.ui.get_user_choice("\nSelect a category:", self.categories)
        if category is None:
            return
        category -= 1
        content = self.catalog_manager.add(category)
        if content:
            self.catalog[category].append(content)
            self.ui.console_output("Content added successfully.")

    def edit_content(self):
        category = self.ui.get_user_choice("\nSelect a category to edit:", self.categories)
        if category is None:
            return
        self.catalog_manager.edit(category - 1)

    def remove_content(self):
        category = self.ui.get_user_choice("\nSelect a category to remove from:", self.categories)
        if category is None:
            return
        self.catalog_manager.remove(category - 1)

    def search_content(self):
        category = self.ui.get_user_choice("\nSelect a category to search:", self.categories)
        if category is None:
            return

        attribute = self.ui.get_user_choice("\nSelect an attribute to search by:", self.attributes)
        if attribute is None:
            return

        search_value = self.ui.get_user_input(f"\nEnter the {self.attributes[attribute]} to search for: ")
        found_items = self.catalog_manager.search(category - 1, attribute, search_value)

        if found_items:
            self.ui.console_output("\nFound items:")
            for item in found_items:
                self.ui.console_output(str(item))
        else:
            self.ui.console_output(f"\nNo items found with {self.attributes[attribute]} = '{search_value}'.")

    def display_catalog(self):
        self.catalog_manager.display()

    def exit_program(self):
        save_data(self.catalog)
        self.ui.console_output("\nData saved. Exiting program.")
        exit()
