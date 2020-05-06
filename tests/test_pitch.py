import unittest
from app.models import Pitch,User
from app import db


def setUp(self):
     self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
    self.new_pitch = Pitch(pitch_title = "pitch one", pitch_description = "afddbabbdb",pitch_category='Business')

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.movie_id,12345)
        self.assertEquals(self.new_pitch.movie_title,'Review for movies')
        self.assertEquals(self.new_pitch.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_pitch.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_pitch.user,self.user_James)