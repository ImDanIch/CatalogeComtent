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