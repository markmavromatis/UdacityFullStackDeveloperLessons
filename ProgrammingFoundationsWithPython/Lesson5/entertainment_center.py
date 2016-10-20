import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")


school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

when_harry_met_sally = media.Movie("When Harry Met Sally",
                                   "Boy meets girl several times, then falls in love",
                                   "https://upload.wikimedia.org/wikipedia/en/1/1c/WhenHarryMetSallyPoster.jpg",
                                   "https://www.youtube.com/watch?v=vmSpCLefjnw")

before_sunrise = media.Movie("Before Sunrise",
                                   "Boy meets girl on train...",
                                   "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                                   "https://www.youtube.com/watch?v=9v6X-Dytlko")

before_sunset = media.Movie("Before Sunset",
                                   "Boy reunites with girl after 10-years...",
                                   "https://upload.wikimedia.org/wikipedia/en/d/d1/Before_Sunset_poster.jpg",
                                   "https://www.youtube.com/watch?v=oI3UuneLcyU")


movies = [before_sunrise, before_sunset, toy_story, avatar,
          when_harry_met_sally, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games]

# fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

