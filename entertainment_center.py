# This is the main file to be run. 
# The project consists of building a website showcasing my favourite movies where we can watch the trailer of each
# It has 6 instances (6 movies)

import media
import fresh_tomatoes

# we have below 6 instanes with their corresponding content. 
# Each instance contains the title, a storyline, the link to to the picture and the link to the trailer

toy_story = media.Movie("Toy story", 
						"A story of a boy and his toys",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=TZeG23jEfHM")
avatar = media.Movie("Avatar", 
					 "A marine on an alien planet", 
					 "http://media.hollywood.com/images/679x1000/7037214.jpg", 
					 "https://www.youtube.com/watch?v=cX0R3mXaod8")
dory = media.Movie("Finding dory", 
				   "A fish that is more than a fish", 
				   "http://cinemalive.in/wp-content/uploads/2016/03/finding-dory.png",
				   "https://www.youtube.com/watch?v=3JNLwlcPBPI")
nemo = media.Movie("Finding nemo", 
				   "A fish", 
				   "http://www.albuquerquecc.com/uploads/CalendarV2/b428551809b744f8b533b979fb60db33/pva6ds.jpeg",
				   "https://www.youtube.com/watch?v=wZdpNglLbt8")
hercules = media.Movie("Hercules",
					   "Hercules the master",
					   "https://upload.wikimedia.org/wikipedia/en/0/09/Hercules_(2014_film).jpg",
					   "https://www.youtube.com/watch?v=1L41RWI1oUg")
batman = media.Movie("Batman under the Hood", 
					 "Batman the superhero", 
					 "http://cdn.collider.com/wp-content/uploads/2015/10/batman-under-the-red-hood-poster.jpg",
					 "https://www.youtube.com/watch?v=1T__uN5xmC0")


# We create an array with every instance in it so we can call open_movies_page
movies = [toy_story, avatar, dory, nemo, hercules, batman]

fresh_tomatoes.open_movies_page(movies)

