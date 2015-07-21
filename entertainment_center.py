# -*- coding: cp1252 -*-
import redbox
import media

forrest_gump = media.Movie("Forrest Gump",
                        "Life of Forrest Gump, a slow-witted and naïve, but good-hearted and athletically prodigious man",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")

fast_and_furious7 = media.Movie("Fast And Furious 7",
                        "street clubs that race Japanese cars late at night",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Fast_and_Furious_Poster.jpg/220px-Fast_and_Furious_Poster.jpg",
                        "https://www.youtube.com/watch?v=hcYKNIEj7co")

minions = media.Movie("Minions",
                        "Minions are small, yellow pill-shaped creatures who have existed since the beginning of time",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Minions_poster.jpg/220px-Minions_poster.jpg",
                        "https://www.youtube.com/watch?v=dVDk7PXNXB8")

wedding_ringer = media.Movie("Wedding Ringer",
                        "Jimmy Callahan (Kevin Hart) provides best man services for guys who don't have the friends necessary for a wedding",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/TheWeddingRingerPoster.jpg/220px-TheWeddingRingerPoster.jpg",
                        "https://www.youtube.com/watch?v=KG5CnCgnplU")

midnight_in_Paris = media.Movie("Midnight in Paris",
                        "Gil Pender, a successful but creatively unfulfilled Hollywood screenwriter, and his fiancée, Inez, are in Paris, vacationin",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger games",
                        "The Hunger Games trilogy takes place in an unspecified future time in a dystopian post-apocalyptic nation of Panem,",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=KmYNkasYthg")

movies = [forrest_gump, fast_and_furious7, minions, wedding_ringer, midnight_in_Paris, hunger_games]



redbox.open_movies_page(movies)


