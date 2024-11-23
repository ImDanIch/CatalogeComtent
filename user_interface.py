class UserInterface:
    def handle_user_interaction(self, action, message, options=None):
        if action == 'output':
            print(message)

        elif action == 'input':
            return input(message)

        elif action == 'choice' and options:
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
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif action == 'error':
            print(f"Error: {message}")

        else:
            raise ValueError("Invalid action type specified.")

    def validate_year(self, value, current_year):
        if value.isdigit():
            year = int(value)
            return 1400 <= year <= current_year
        return False

    def validate_positive_number(self, value):
        return value.isdigit() and int(value) > 0

    def get_valid_input(self, prompt, validation_function, error_message, *args):
        while True:
            value = self.handle_user_interaction('input', prompt)
            if validation_function(value, *args):
                return value
            self.handle_user_interaction('error', error_message)

    def select_item_from_list(self, items, prompt):
        if not items:
            self.handle_user_interaction('output', "No items available.")
            return None

        self.handle_user_interaction('output', prompt)
        for i, item in enumerate(items, start=1):
            self.handle_user_interaction('output', f"{i}: {item.name}")

        while True:
            try:
                choice = int(self.handle_user_interaction('input',
                                                             "Enter the number of the item or 0 to go back: "))
                if choice == 0:
                    return None
                if 1 <= choice <= len(items):
                    return items[choice - 1]
                else:
                    self.handle_user_interaction('error', "Invalid number. Please try again.")
            except ValueError:
                self.handle_user_interaction('error', "Input must be a number. Please try again.")