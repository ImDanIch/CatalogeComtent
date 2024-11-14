import json

#Список жанрів для фільмів та серіалів
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

#Список жанрів для музики
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

    #Функція для запису об'єкта у файл
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
        return f"{super().__str__()}"


class TVShow(MediaContent):
    def __init__(self, name, genre, release_year, creator):
        super().__init__(name, genre, release_year, creator)

    def __str__(self):
        return f"{super().__str__()}"


class Music(MediaContent):
    def __init__(self, name, genre, release_year, creator):
        super().__init__(name, genre, release_year, creator)

    def __str__(self):
        return f"{super().__str__()}"


class Catalog:
    def __init__(self):
        self.movies = []
        self.tv_shows = []
        self.music = []

    def add(self, content):
        if isinstance(content, Movie):
            self.movies.append(content)
        elif isinstance(content, TVShow):
            self.tv_shows.append(content)
        elif isinstance(content, Music):
            self.music.append(content)
        self.save_data()

    def save_data(self):
        data = {
            'movies': [],
            'tv_shows': [],
            'music': [],
        }
        for movie in self.movies:
            data['movies'].append(movie.to_dict())
        for tv_show in self.tv_shows:
            data['tv_shows'].append(tv_show.to_dict())
        for music_item in self.music:
            data['music'].append(music_item.to_dict())

        with open('catalog_data.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open('catalog_data.json', 'r') as file:
                data = json.load(file)

                self.movies = []
                for movie in data['movies']:
                    self.movies.append(Movie(
                        name=movie['name'],
                        genre=movie['genre'],
                        release_year=movie['release_year'],
                        creator=movie['creator']
                    ))

                self.tv_shows = []
                for tv_show in data['tv_shows']:
                    self.tv_shows.append(TVShow(
                        name=tv_show['name'],
                        genre=tv_show['genre'],
                        release_year=tv_show['release_year'],
                        creator=tv_show['creator']
                    ))

                self.music = []
                for music_item in data['music']:
                    self.music.append(Music(
                        name=music_item['name'],
                        genre=music_item['genre'],
                        release_year=music_item['release_year'],
                        creator=music_item['creator']
                    ))

        except FileNotFoundError:
            pass

    #Виведення пового каталогу
    def display_catalog(self):
        print("Movies:")
        for movie in self.movies:
            print(movie)
        print("\nTV Shows:")
        for tv_show in self.tv_shows:
            print(tv_show)
        print("\nMusic:")
        for music_item in self.music:
            print(music_item)


def select_genre(arr):
    for i, genre in arr.items():
        print(f"{i}. {genre}")
    genre_num = int(input("Choice genre:: "))
    return arr.get(genre_num, "Invalid choice. Please try again.")


catalog = Catalog()
catalog.load_data()

while True:
    print("\nMain Menu:")
    print("2. Add content")
    print("3. Remove content")
    print("3. Search content")
    print("4. Display catalog")
    print("0. Exit")
    choice = input("Choose an option: ")

    #Для додавання контенту
    if choice == '2':
        print("\nChoose category to add:")
        print("2. Movie")
        print("3. TV Show")
        print("3. Music")
        print("0. Exit")
        category = input("Category: ")

        if category == '0':
            continue

        if category == '2':
            name = input("Enter movie name: ")
            genre = select_genre(genres)
            release_year = int(input("Enter release year: "))
            creator = input("Enter director: ")
            content = Movie(name, genre, release_year, creator)
        elif category == '3':
            name = input("Enter TV show name: ")
            genre = select_genre(genres)
            release_year = int(input("Enter release year: "))
            creator = input("Enter creator: ")
            content = TVShow(name, genre, release_year, creator)
        elif category == '3':
            name = input("Enter music name: ")
            genre = select_genre(music_genres)
            release_year = int(input("Enter release year: "))
            creator = input("Enter artist: ")
            content = Music(name, genre, release_year, creator)

        catalog.add(content)

    #Для видалення контенту
    elif choice == '3':
        pass

    #Для пошуку контенту по властивості
    elif choice == '3':
        pass

    #Для виведення пового каталогу
    elif choice == '4':
        catalog.display_catalog()

    elif choice == '0':
        catalog.save_data()
        print("Exiting and saving data.")
        break