from file_manager import load_data, save_data
from options_data import categories, attributes, genres, music_genres, commands
from user_interface import UserInterface
from command_handler import CommandHandler


def main():
    catalog = load_data()
    ui = UserInterface()
    handler = CommandHandler(catalog, ui, categories, genres, music_genres, attributes)

    while True:
        try:
            command = ui.get_user_choice("\nChoose a command:", commands)
            if command is None:
                ui.console_output("Exiting program. Goodbye!")
                break
            handler.execute_command(command)
        except ValueError:
            ui.console_output_error("Command must be a number. Please try again.")
        except Exception as e:
            ui.console_output_error(f"An unexpected error occurred: {e}")

    save_data(catalog)


if __name__ == "__main__":
    main()
