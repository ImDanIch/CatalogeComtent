from datetime import datetime


class UserInterface:
    def get_user_input(self, message):
        return input(message)

    def console_output(self, message):
        print(message)

    def console_output_error(self, message):
        print(f"Error: {message}")

    def get_user_choice(self, message, options):
        print(message)
        for key, value in options.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    return None
                if choice in options:
                    return choice
                else:
                    print(f"Invalid input. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def validate_year(self, value):
        current_year = datetime.now().year
        if value.isdigit():
            year = int(value)
            return 1400 <= year <= current_year
        return False

    def validate_positive_number(self, value):
        return value.isdigit() and int(value) > 0

    def get_valid_input(self, prompt, validation_function):
        while True:
            value = self.get_user_input(prompt)
            if validation_function(value):
                return value
            self.console_output_error("Invalid input. Please try again.")

    def select_item_from_list(self, items, prompt):
        if not items:
            self.console_output_error("No items available.")
            return None

        self.console_output(prompt)
        for i, item in enumerate(items, start=1):
            self.console_output(f"{i}: {item.name}")

        while True:
            try:
                choice = int(self.get_user_input("Enter the number of the item or 0 to go back: "))
                if choice == 0:
                    return None
                if 1 <= choice <= len(items):
                    return items[choice - 1]
                else:
                    self.console_output_error("Invalid number. Please try again.")
            except ValueError:
                self.console_output_error("Input must be a number. Please try again.")
