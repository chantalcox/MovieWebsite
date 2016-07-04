#We have here all the instance variables and the instance method

import webbrowser

class Movie():
	
#We use the term "udacity" instead of "self" in this code because we are not allowed in Python to use "self"
	def __init__ (udacity, movie_title, movie_storyline, poster_image, trailer_youtube):
		udacity.title = movie_title
		udacity.storyline= movie_storyline
		udacity.poster_image_url = poster_image
		udacity.trailer_youtube_url = trailer_youtube

#below is the instance method

	def show_trailer(udacity):
		webbrowser.open(udacity.trailer_youtube_url)