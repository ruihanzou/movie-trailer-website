__author__ = 'ruihanzou'
import webbrowser

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube):
        """
        A Movie class with title, storyline, image and trailer attributes.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        You can watch a movie trailer by calling show_trailer method.
        """
        webbrowser.open(self.trailer_youtube_url)
