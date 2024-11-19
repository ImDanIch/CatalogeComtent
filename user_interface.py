class UserInterface:
    def choose_option(self, options, option_name):
        print(f"\nChoose {option_name}:")
        for i, option in options.items():
            print(f"{i}: {option}")
        while True:
            try:
                choice = int(input(f"Enter number for {option_name}: "))
                if choice == 0:
                    return None
                elif choice in options:
                    return choice
                else:
                    print(f"\nError: Invalid {option_name}. Please try again.\n")
            except ValueError:
                print(f"\nError: {option_name} must be a number. Please try again.\n")
