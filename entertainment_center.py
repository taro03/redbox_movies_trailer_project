# -*- coding: cp1252 -*-
#import redbox which contain a function to open the movies page
import redbox

#import media file contain class Movie
import media

#create instance from class Movie: Forrest Gump
forrest_gump = media.Movie(
    "Forrest Gump",
    "Stars: Tom Hanks, Robin Wright, Gary Sinise",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=uPIEn0M8su0"
    )
    
#create instance from class Movie: Fast and Furious 7
fast_and_furious7 = media.Movie(
    "Fast And Furious 7",
    "Stars: Vin Diesel, Paul Walker, Dwayne Johnson",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Fast_and_Furious_Poster.jpg/220px-Fast_and_Furious_Poster.jpg",
    "https://www.youtube.com/watch?v=hcYKNIEj7co"
    )

#create instance from class Movie: Minions
minions = media.Movie(
    "Minions",
    "Stars: Sandra Bullock, Jon Hamm, Michael Keaton ",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Minions_poster.jpg/220px-Minions_poster.jpg",
    "https://www.youtube.com/watch?v=dVDk7PXNXB8"
    )

#create instance from class Movie: The Wedding Ringer
wedding_ringer = media.Movie(
    "Wedding Ringer",
    "Stars: Kevin Hart, Josh Gad, Kaley Cuoco-Sweeting ",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/TheWeddingRingerPoster.jpg/220px-TheWeddingRingerPoster.jpg",
    "https://www.youtube.com/watch?v=KG5CnCgnplU"
    )

#create instance from class Movie: Midnight in Paris
midnight_in_Paris = media.Movie(
    "Midnight in Paris",
    "Stars: Owen Wilson, Rachel McAdams, Kathy Bates",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=FAfR8omt-CY"
    )

#create instance from class Movie: The Hunger Games
hunger_games = media.Movie(
    "Hunger games",
    "Stars: Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=KmYNkasYthg"
    )

#create a list of movies
movies = [
    forrest_gump,
    fast_and_furious7,
    minions,
    wedding_ringer,
    midnight_in_Paris,
    hunger_games
    ]

#called out function from redbox file to open the movies page
redbox.open_movies_page(movies)
