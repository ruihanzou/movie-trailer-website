# -*- coding: utf-8 -*-
author__= 'ruihanzou'
"""
open the web browser with 6 customized movies. 
"""
import media
import fresh_tomatoes

the_pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "The Pursuit of Happyness is a 2006 American biographical drama film \
    based on Chris Gardner's nearly one-year struggle with homelessness.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg",
    "https://youtu.be/SYg7RRYKWGw")
catch_me_if_you_can = media.Movie(
    "Catch Me If you can",
    "Story based on the life of Frank Abagnale, who, before his 19th birthday, \
    successfully performed cons worth millions of dollars by posing as \
    a Pan American World Airways pilot, a Georgia doctor, \
    and a Louisiana parish prosecutor..",
    "http://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Catch_Me_If_You_Can_2002_movie.jpg/220px-Catch_Me_If_You_Can_2002_movie.jpg",
    "https://youtu.be/71rDQ7z4eFg")

the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "The story of Andy Dufresne, a banker who is sentenced \
    to life in ShawshankState Prison..",
    "http://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
    "https://youtu.be/eGfAj9ZJymo")

ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

harry_potter = media.Movie(
    "Harry Potter and the Philosopher's Stone",
    "The story follows Harry Potter's first year at Hogwarts as he discovers \
    that he is a famous wizard and begins his magical education.",
    "http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SY317_CR8,0,214,317_AL_.jpg",
    "https://youtu.be/PbdM1db3JbY")

furious_7 = media.Movie(
    "Furious 7",
    "Furious 7 follows Dominic Toretto (Diesel), Brian O'Conner (Walker) \
    and the rest of their team, who have returned to the United States \
    to live normal lives after securing amnesties for their past crimes..",
    "http://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
    "https://youtu.be/yISKeT6sDOg")
movies = [the_pursuit_of_happyness, catch_me_if_you_can,
          the_shawshank_redemption, ratatouille, harry_potter, furious_7]
fresh_tomatoes.open_movies_page(movies)
