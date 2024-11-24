import unittest
from unittest.mock import patch, MagicMock
from user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.ui = UserInterface()

    @patch("builtins.input", return_value="2")
    def test_handle_user_interaction_choice(self, mock_input):
        options = {1: "Option 1", 2: "Option 2"}
        result = self.ui.handle_user_interaction("choice", "Choose an option:", options)
        self.assertEqual(result, 2)
        mock_input.assert_called_once_with("Enter your choice: ")

    @patch("builtins.input", return_value="Some input")
    def test_handle_user_interaction_input(self, mock_input):
        result = self.ui.handle_user_interaction("input", "Enter a value:")
        self.assertEqual(result, "Some input")
        mock_input.assert_called_once_with("Enter a value:")

    @patch("builtins.print")
    def test_handle_user_interaction_output(self, mock_print):
        self.ui.handle_user_interaction("output", "Test message")
        mock_print.assert_called_once_with("Test message")

    @patch("builtins.print")
    def test_handle_user_interaction_error(self, mock_print):
        self.ui.handle_user_interaction("error", "An error occurred")
        mock_print.assert_called_once_with("Error: An error occurred")

    @patch("builtins.input", side_effect=["2000", "abcd", "1500"])
    def test_get_valid_input(self, mock_input):
        def validate_year(value, current_year):
            return value.isdigit() and 1400 <= int(value) <= current_year

        result = self.ui.get_valid_input(
            "Enter a year: ",
            validate_year,
            "Year must be between 1400 and current year.",
            2023
        )
        self.assertEqual(result, "2000")
        self.assertEqual(mock_input.call_count, 1)

    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    def test_select_item_from_list(self, mock_print, mock_input):
        items = [
            MagicMock(name="Item 1", **{"name": "First"}),
            MagicMock(name="Item 2", **{"name": "Second"}),
        ]

        result = self.ui.select_item_from_list(items, "Choose an item:")
        self.assertEqual(result.name, "First")
        mock_print.assert_any_call("1: First")
        mock_print.assert_any_call("2: Second")

    @patch("builtins.input", side_effect=["-1", "3", "2"])
    @patch("builtins.print")
    def test_handle_user_interaction_choice_invalid(self, mock_print, mock_input):
        options = {1: "Option 1", 2: "Option 2"}
        result = self.ui.handle_user_interaction("choice", "Choose an option:", options)
        self.assertEqual(result, 2)
        self.assertEqual(mock_input.call_count, 3)
        mock_print.assert_any_call("Invalid choice. Please try again.")


if __name__ == "__main__":
    unittest.main()
