# Discussion Assignment Oct 24


# Check if ADD, EDIT, SHOW, DELETE, EXIT exist

# convert_list_dictionary
# can test if list has 6 elements; fail otherwise
# can test if you are taking in a list

# show_movies
# check if a list of movies are in the pyflix dictionary


## TESTING ##
from pyflix import *
import unittest

class MovieTest(unittest.TestCase):
    def SetUp(self):
        with open("out.txt", 'r') as f:
            self.out = f.read()
    def test_AllMoviesPresent(self):
        pyflix = {}
        # running from my program
        preload(pyflix)
        movies = list(pyflix.keys())
        # if this fails, whole test fails
        assertIn("Batman", self.out)

# These are some changes for practicing Github! Whooo!!! 
