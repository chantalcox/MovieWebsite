#We have here all the instane variables and the instance method

import webbrowser

class Movie():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__ (udacity, movie_title, movie_storyline, poster_image, trailer_youtube):
		udacity.title = movie_title
		udacity.storyline= movie_storyline
		udacity.poster_image_url = poster_image
		udacity.trailer_youtube_url = trailer_youtube

	def show_trailer(udacity):
		webbrowser.open(udacity.trailer_youtube_url)