import unittest
from catalog import Movie, TVShow
from catalog_manager import CatalogManager


class TestCatalogManager(unittest.TestCase):
    def setUp(self):
        self.catalog = [[], [], []]
        self.categories = {1: "Movie", 2: "TV show", 3: "Music"}
        self.genres = {1: "Action", 2: "Drama"}
        self.music_genres = {1: "Pop", 2: "Rock"}

        self.manager = CatalogManager(self.catalog, self.categories, self.genres, self.music_genres)

    def test_add_movie(self):
        movie = Movie("Inception", "Sci-Fi", 2010, "Christopher Nolan")
        self.catalog[0].append(movie)
        self.assertEqual(len(self.catalog[0]), 1)
        self.assertEqual(self.catalog[0][0].name, "Inception")

    def test_add_tv_show(self):
        tv_show = TVShow("Breaking Bad", "Drama", 2008, "Vince Gilligan", 5, 62)
        self.catalog[1].append(tv_show)
        self.assertEqual(len(self.catalog[1]), 1)
        self.assertEqual(self.catalog[1][0].season, 5)

    def test_remove_item(self):
        movie = Movie("Inception", "Sci-Fi", 2010, "Christopher Nolan")
        self.catalog[0].append(movie)
        self.manager.remove(1)
        self.assertEqual(len(self.catalog[0]), 0)

    def test_search_item(self):
        movie = Movie("Inception", "Sci-Fi", 2010, "Christopher Nolan")
        self.catalog[0].append(movie)

        result = self.manager.search(1, 1, "Inception")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Inception")

    def test_edit_item(self):
        movie = Movie("Inception", "Sci-Fi", 2010, "Christopher Nolan")
        self.catalog[0].append(movie)

        movie.name = "Inception Updated"
        self.assertEqual(self.catalog[0][0].name, "Inception Updated")

    def test_display(self):
        movie = Movie("Inception", "Sci-Fi", 2010, "Christopher Nolan")
        self.catalog[0].append(movie)
        tv_show = TVShow("Breaking Bad", "Drama", 2008, "Vince Gilligan", 5, 62)
        self.catalog[1].append(tv_show)

        with self.assertLogs() as log:
            self.manager.display()
        self.assertIn("Inception", log.output[0])
        self.assertIn("Breaking Bad", log.output[1])


if __name__ == "__main__":
    unittest.main()
