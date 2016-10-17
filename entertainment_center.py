import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        0,
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     0,
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

walking_dead = media.Movie("The Walking Dead",
                           0,
                           "Sheriff wakes up from coma during the zombie apocalypse",
                           "https://upload.wikimedia.org/wikipedia/en/1/17/The_Walking_Dead_title_card.jpg",
                           "https://www.youtube.com/watch?v=R1v0uFms68U")

school_of_rock = media.Movie("School of Rock",
                             0,
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          0,
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                0,
                                "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("The Hunger Games",
                           0,
                           "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, walking_dead, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
