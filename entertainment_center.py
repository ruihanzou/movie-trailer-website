__author__ = 'ruihanzou'
import media
import fresh_tomatoes

the_pursuit_of_happyness = media.Movie("The Pursuit of Happyness", "The Pursuit of Happyness is a 2006 American biographical drama film based on Chris Gardner's nearly one-year struggle with homelessness. Directed by Gabriele Muccino, the film features Will Smith as Gardner, a homeless salesman. Smith's son Jaden Smith co-stars, making his film debut as Gardner's son, Christopher Jr. Will Smith and Jaden Smith later appeared together in the film After Earth.",
                                       "http://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg",
                                       "https://youtu.be/SYg7RRYKWGw")
catch_me_if_you_can = media.Movie("Catch Me If you can", "Catch Me If You Can is a 2002 American biographical crime drama film based on the life of Frank Abagnale, who, before his 19th birthday, successfully performed cons worth millions of dollars by posing as a Pan American World Airways pilot, a Georgia doctor, and a Louisiana parish prosecutor. His primary crime was check fraud; he became so experienced that the FBI eventually turned to him to help in catching other check forgers. The film was directed by Steven Spielberg and stars Leonardo DiCaprio and Tom Hanks, with Christopher Walken, Martin Sheen, and Nathalie Baye in supporting roles.",
"http://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Catch_Me_If_You_Can_2002_movie.jpg/220px-Catch_Me_If_You_Can_2002_movie.jpg",
"https://youtu.be/71rDQ7z4eFg")

the_shawshank_redemption = media.Movie("The Shawshank Redemption", "The story of Andy Dufresne, a banker who is sentenced to life in Shawshank State Prison for the murder of his wife and her lover despite his claims of innocence. During his time at the prison, he befriends a fellow inmate, Ellis Boyd ‘Red’ Redding, and finds himself protected by the guards after the warden begins using him in his money laundering operation.",
"http://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
"https://youtu.be/eGfAj9ZJymo")

ratatouille = media.Movie("Ratatouille", "Storyline",
"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
"https://www.youtube.com/watch?v=c3sBBRxDAqk")

harry_potter = media.Movie("Harry Potter and the Philosopher's Stone", "The story follows Harry Potter's first year at Hogwarts as he discovers that he is a famous wizard and begins his magical education.",
"http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SY317_CR8,0,214,317_AL_.jpg",
"https://youtu.be/PbdM1db3JbY")

furious_7 = media.Movie("Furious 7", "Furious 7 follows Dominic Toretto (Diesel), Brian O'Conner (Walker) and the rest of their team, who have returned to the United States to live normal lives after securing amnesties for their past crimes in Fast & Furious 6 (2013), until Deckard Shaw (Statham), a rogue special forces assassin seeking to avenge his comatose younger brother, puts them in danger once again.",
"http://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
"https://youtu.be/yISKeT6sDOg")
movies = [the_pursuit_of_happyness, catch_me_if_you_can, the_shawshank_redemption, ratatouille, harry_potter, furious_7 ]
fresh_tomatoes.open_movies_page(movies)
