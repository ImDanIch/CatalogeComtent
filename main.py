from file_manager import load_data
from options_data import categories, attributes, genres, music_genres, commands
from user_interface import UserInterface
from command_handler import CommandHandler


def main():
    catalog = load_data()
    ui = UserInterface()
    handler = CommandHandler(catalog, ui, categories, genres, music_genres, attributes)

    while True:
        try:
            command = ui.handle_user_interaction('choice', "\nChoose a command:", commands)
            handler.execute_command(command)
        except ValueError:
            ui.handle_user_interaction('error', "\nCommand must be a number. Please try again.")


if __name__ == "__main__":
    main()
