import json
from datetime import datetime


commands = {
    0: "Save and exit",
    1: "Add",
    2: "Edit",
    3: "Remove",
    4: "Search",
    5: "Display catalog"
}

categories = {
    0: "Back",
    1: "Movie",
    2: "TV show",
    3: "Music",
}

attributes = {
    0: "Back",
    1: "Name",
    2: "Genre",
    3: "Release year",
    4: "Creator"
}

genres = {
    1: "Action",
    2: "Adventure",
    3: "Animation",
    4: "Comedy",
    5: "Crime",
    6: "Drama",
    7: "Fantasy",
    8: "Historical",
    9: "Horror",
    10: "Musical",
    11: "Mystery",
    12: "Romance",
    13: "Sci-Fi",
    14: "Thriller",
    15: "War"
}

music_genres = {
    1: "Blues",
    2: "Classical",
    3: "Country",
    4: "Electronic",
    5: "Hip-Hop",
    6: "Jazz",
    7: "Metal",
    8: "Pop",
    9: "Reggae",
    10: "Rock"
}


class MediaContent:
    def __init__(self, name, genre, release_year, creator):
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.creator = creator

    def __str__(self):
        return f"{self.name} ({self.release_year}), Genre: {self.genre}, Creator: {self.creator}"

    def to_dict(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'release_year': self.release_year,
            'creator': self.creator
        }


class Movie(MediaContent):
    def __init__(self, name, genre, release_year, creator):
        super().__init__(name, genre, release_year, creator)

    def __str__(self):
        return f"{super().__str__()}."


class TVShow(MediaContent):
    def __init__(self, name, genre, release_year, creator, season, series):
        super().__init__(name, genre, release_year, creator)
        self.season = season
        self.series = series

    def __str__(self):
        return f"{super().__str__()}, Season: {self.season}, Series: {self.series}."

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'season': self.season,
            'series': self.series
        })
        return data


class Music(MediaContent):
    def __init__(self, name, genre, release_year, creator, album):
        super().__init__(name, genre, release_year, creator)
        self.album = album

    def __str__(self):
        return f"{super().__str__()}, Album: {self.album}."

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'album': self.album
        })
        return data


class Catalog:
    def __init__(self):
        self.movies = []
        self.tv_shows = []
        self.music = []

    def save_data(self):
        data = {
            'movies': [],
            'tv_shows': [],
            'music': [],
        }
        for i in self.movies:
            data['movies'].append(i.to_dict())
        for i in self.tv_shows:
            data['tv_shows'].append(i.to_dict())
        for i in self.music:
            data['music'].append(i.to_dict())

        with open('catalog_data.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open('catalog_data.json', 'r') as file:
                data = json.load(file)

                self.movies = []
                for i in data['movies']:
                    self.movies.append(Movie(
                        name=i['name'],
                        genre=i['genre'],
                        release_year=i['release_year'],
                        creator=i['creator']
                    ))

                self.tv_shows = []
                for i in data['tv_shows']:
                    self.tv_shows.append(TVShow(
                        name=i['name'],
                        genre=i['genre'],
                        release_year=i['release_year'],
                        creator=i['creator'],
                        season=i['season'],
                        series=i['series']
                    ))

                self.music = []
                for i in data['music']:
                    self.music.append(Music(
                        name=i['name'],
                        genre=i['genre'],
                        release_year=i['release_year'],
                        creator=i['creator'],
                        album=i['album']
                    ))

        except FileNotFoundError:
            pass

    def menu(self, dict, name_dict):
        print(f"\nChoose {name_dict}:")
        for i in dict:
            print(f"{i}: {dict[i]}")

        while True:
            try:
                num = int(input(f"Enter number of {name_dict}: "))
                if num == 0:
                    return None
                elif dict.get(num):
                    break
                else:
                    print(f"\nError, {name_dict} is unavailable. Please try again.\n")
            except ValueError:
                print(f"\nError, {name_dict} must be a number. Please try again.\n")
        return num

    def display_catalog(self):
        print("Movies:")
        for i in self.movies:
            print(i)
        print("\nTV Shows:")
        for i in self.tv_shows:
            print(i)
        print("\nMusic:")
        for i in self.music:
            print(i)

    def add(self, ):
        current_year = datetime.now().year
        category = catalog.menu(categories, "category")
        if category is None:
            return

        category = categories[category]
        name = input(f"Enter {category} name: ")
        while True:
            try:
                realise_year = int(input(f"Enter realise year: "))
                if realise_year > current_year or realise_year < 1400:
                    print(f"\nError, realise year is unavailable. Please try again.\n")
                else:
                    break
            except ValueError:
                print(f"\nError, realise year must be a number. Please try again.\n")
        creator = input("Enter creator: ")
        if category == "Music":
            genre = genres[catalog.menu(music_genres, "genre")]
            album = input("Enter album: ")
            content = Music(name, genre, realise_year, creator, album)
            self.music.append(content)

        elif category == "TV show":
            genre = genres[catalog.menu(genres, "genre")]
            while True:
                try:
                    season = int(input("Enter season: "))
                    break
                except ValueError:
                    print(f"\nError, season must be a number. Please try again.\n")

            while True:
                try:
                    series = int(input("Enter series: "))
                    break
                except ValueError:
                    print(f"\nError, series must be a number. Please try again.\n")
            content = TVShow(name, genre, realise_year, creator, season, series)
            self.tv_shows.append(content)
        else:
            genre = genres[catalog.menu(genres, "genre")]
            content = Movie(name, genre, realise_year, creator)
            self.movies.append(content)

    def edit(self):
        pass

    def remove(self):
        category = catalog.menu(categories, "category")
        if category is None:
            return

        category_arr = {
            1: self.movies,
            2: self.tv_shows,
            3: self.music
        }

        arr = category_arr.get(category)

        category = categories[category]
        if not arr:
            print(f"\nNo items available in {category}.\n")
            return

        print("\nSelect an item to remove:")
        i = 1
        for item in arr:
            print(f"{i}: {item}")
            i += 1

        while True:
            try:
                i = int(input("Enter the item number to remove or 0 to go back: "))
                if i == 0:
                    return
                elif 1 <= i <= len(arr):
                    item = arr[i - 1]
                    que = input(f"Are you sure you want to delete '{item}'? (y/n): ").lower()
                    if que == 'y':
                        arr.pop(i - 1)
                        print("Item removed successfully.")
                    else:
                        print("Deletion canceled.")
                    break
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def search(self):
        category = catalog.menu(categories, "category")
        if category is None:
            return

        category_arr = {
            1: self.movies,
            2: self.tv_shows,
            3: self.music
        }

        arr = category_arr.get(category)

        attr_num = catalog.menu(attributes, "parameter")
        if attr_num is None:
            return
        attr_name = attributes.get(attr_num)

        search_value = input(f"Enter the {attr_name} to search for: ").strip()

        found_items = []
        for item in arr:
            if hasattr(item, attr_name.lower()):
                if str(getattr(item, attr_name.lower())).lower() == search_value.lower():
                    found_items.append(item)

        if found_items:
            print("\nFound items:")
            for i, found_item in enumerate(found_items, start=1):
                print(f"{i}: {found_item}")
        else:
            print(f"No items found with {attr_name} = '{search_value}' in {category}.")


catalog = Catalog()
catalog.load_data()
num = catalog.menu(commands, "command")
while num is not None:
    if num == 1:
        catalog.add()
    elif num == 2:
        catalog.edit()
    elif num == 3:
        catalog.remove()
    elif num == 4:
        catalog.search()
    elif num == 5:
        catalog.display_catalog()
    elif num == 0:
        break
    num = catalog.menu(commands, "command")
catalog.save_data()