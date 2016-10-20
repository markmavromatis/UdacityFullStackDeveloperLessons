import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
print(avatar.storyline)

# avatar.show_trailer()

when_harry_met_sally = media.Movie("When Harry Met Sally",
                                   "Boy meets girl several times, then falls in love",
                                   "https://en.wikipedia.org/wiki/File:WhenHarryMetSallyPoster.jpg",
                                   "https://www.youtube.com/watch?v=vmSpCLefjnw")

# when_harry_met_sally.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

