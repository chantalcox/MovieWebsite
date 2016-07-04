#This is the main file to be run
# It has 6 instances (6 movies)

import media
import fresh_tomatoes

toy_story = media.Movie("Toy story", "A story of a boy and his toys", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=TZeG23jEfHM")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://media.hollywood.com/images/679x1000/7037214.jpg", "https://www.youtube.com/watch?v=cX0R3mXaod8")
#print(avatar.storyline)

dory = media.Movie("Finding dory", "A fish that is more than a fish", "http://cinemalive.in/wp-content/uploads/2016/03/finding-dory.png","https://www.youtube.com/watch?v=3JNLwlcPBPI")
#print(dory.storyline)

#avatar.show_trailer()
#dory.show_trailer()

nemo = media.Movie("Finding nemo", "A fish", "http://www.albuquerquecc.com/uploads/CalendarV2/b428551809b744f8b533b979fb60db33/pva6ds.jpeg","https://www.youtube.com/watch?v=wZdpNglLbt8")
hercules = media.Movie("Hercules" , "Hercules the master", "https://upload.wikimedia.org/wikipedia/en/0/09/Hercules_(2014_film).jpg","https://www.youtube.com/watch?v=1L41RWI1oUg")
batman = media.Movie("Batman under the Hood", "Batman the superhero", "http://cdn.collider.com/wp-content/uploads/2015/10/batman-under-the-red-hood-poster.jpg","https://www.youtube.com/watch?v=1T__uN5xmC0")

movies = [toy_story, avatar, dory, nemo, hercules, batman]

print(media.Movie.VALID_RATINGS)