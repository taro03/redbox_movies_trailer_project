#import webbrowser library to open the movies trailer
import webbrowser

#create class Movie contains constrcutor and method
class Movie():
    """create constructor contains information about a movie """
    def __init__(self, movie_title, movie_storyline, poster_image,
               trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    """create a method that open the movie trailer with
    link from the consstructor"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
