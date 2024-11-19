class MediaContent:
    def __init__(self, name, genre, release_year, creator):
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.creator = creator

    def __str__(self):
        return f"{self.name} ({self.release_year}, Genre: {self.genre}, Creator: {self.creator})"

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
        return f"{super().__str__()}, Seasons: {self.season}, Series: {self.series}."

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
