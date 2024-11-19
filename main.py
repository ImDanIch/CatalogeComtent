from file_manager import save_data, load_data
from object_operation import add_content, remove_content, search_content, display_catalog
from options_data import categories, attributes, genres, music_genres, commands
from user_interface import UserInterface

ui = UserInterface()


def main():
    catalog = load_data()

    while True:
        try:
            command = ui.choose_option(commands, "command")

            if command == 1:  # Add Content
                category = ui.choose_option(categories, "category")
                if category is None:
                    continue
                content = add_content(category, categories, genres, music_genres)
                if content:
                    catalog[category].append(content)

            elif command == 2:  # Edit Content
                print("Editing functionality will be added in future updates.")

            elif command == 3:  # Remove Content
                category = ui.choose_option(categories, "category")
                if category is None:
                    continue
                success = remove_content(catalog, category, categories)
                if success:
                    print("Item removed successfully.")

            elif command == 4:  # Search Content
                category = ui.choose_option(categories, "category")
                if category is None:
                    continue
                attribute = ui.choose_option(attributes, "attribute")
                if attribute is None:
                    continue
                search_value = input(f"Enter the {attributes[attribute]} to search for: ")
                found_items = search_content(catalog, category, attribute, search_value)
                if found_items:
                    print("\nFound items:")
                    for item in found_items:
                        print(item)
                else:
                    print(f"No items found with {attributes[attribute]} = '{search_value}' in {categories[category]}.")

            elif command == 5:  # Display Catalog
                display_catalog(catalog)

            elif command is None:  # Save and Exit
                save_data(catalog)
                print("Data saved. Exiting program.")
                break

            else:
                print(f"\nError: Invalid command. Please try again.\n")
        except ValueError:
            print(f"\nError: command must be a number. Please try again.\n")


if __name__ == "__main__":
    main()
