from file_manager import save_data, load_data
from object_operation import add_content,edit_content, remove_content, search_content, display_catalog
from options_data import categories, attributes, genres, music_genres, commands
from user_interface import UserInterface


ui = UserInterface()


def main():
    catalog = load_data()

    while True:
        try:
            command = ui.handle_user_interaction('choice', "\nChoose a command:", commands)

            if command == 1:
                category = ui.handle_user_interaction('choice', "\nSelect a category:", categories)
                if category is None:
                    continue
                content = add_content(category, categories, genres, music_genres)
                if content:
                    catalog[category].append(content)

            elif command == 2:
                category = ui.handle_user_interaction('choice', "\nSelect a category to edit:", categories)
                if category is None:
                    continue
                edit_content(catalog, category, categories)

            elif command == 3:
                category = ui.handle_user_interaction('choice', "\nSelect a category to remove from:", categories)
                if category is None:
                    continue
                success = remove_content(catalog, category, categories)
                if success:
                    ui.handle_user_interaction('output', "\nItem removed successfully.")

            elif command == 4:
                category = ui.handle_user_interaction('choice', "\nSelect a category to search:", categories)
                if category is None:
                    continue
                attribute = ui.handle_user_interaction('choice', "\nSelect an attribute to search by:", attributes)
                if attribute is None:
                    continue
                search_value = ui.handle_user_interaction('input', f"\nEnter the {attributes[attribute]} to search for: ")
                found_items = search_content(catalog, category, attribute, search_value)
                if found_items:
                    ui.handle_user_interaction('output', "\nFound items:")
                    for item in found_items:
                        ui.handle_user_interaction('output', str(item))
                else:
                    ui.handle_user_interaction('output', f"\nNo items found with {attributes[attribute]} = '{search_value}' in {categories[category]}.")

            elif command == 5:
                display_catalog(catalog)

            elif command is None:
                save_data(catalog)
                ui.handle_user_interaction('output', "\nData saved. Exiting program.")
                break

            else:
                ui.handle_user_interaction('error', "\nInvalid command. Please try again.")
        except ValueError:
            ui.handle_user_interaction('error', "\nCommand must be a number. Please try again.")


if __name__ == "__main__":
    main()
