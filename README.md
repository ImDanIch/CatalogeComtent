# Project Title
Multimedia Content Catalog

## Project Description
This software is designed to manage a multimedia content catalog, allowing users to add, edit, delete, and search for information about movies, TV shows, and music. The application is built as a console-based program, following a modular approach, and supports data storage in a JSON file.

## Main Features
- **Content Addition**: Add movies, TV shows, or music albums with relevant attributes.
- **Editing**: Modify the details of a selected object.
- **Deletion**: Remove an entry from the catalog.
- **Search**: Search for objects by category and attributes (e.g., name, genre, release year).
- **Catalog Display**: View all available entries categorized.
- **Data Saving/Loading**: Work with a JSON file to save and load the catalog's state.

## Project Structure
The project consists of the following modules:

- **catalog.py**  
  Implements the `MediaContent`, `Movie`, `TVShow`, and `Music` classes.  
  Defines the data structure for each content type and provides methods for text representation and conversion to dictionaries.

- **command_handler.py**  
  Handles user input and implements the core logic for commands (add, edit, search, delete).

- **file_manager.py**  
  Manages saving and loading data in JSON format through the `save_data` and `load_data` functions.

- **object_operation.py** (likely `CatalogManager`)  
  Manages catalog objects, including their creation, editing, deletion, and searching.

- **user_interface.py**  
  Implements the console interface for user interaction.  
  Handles input/output and validates user input.

- **options_data.py**  
  Contains constants for categories, attributes, genres, and other parameters used in the program.

- **main.py**  
  The entry point of the program. Starts the command processing loop.

## Running the Program
### Requirements:
- Python 3.7 or higher.
- A JSON file (`catalog_data.json`) for saving/loading data (automatically created upon first run).

### Command to run:
```bash
python main.py
