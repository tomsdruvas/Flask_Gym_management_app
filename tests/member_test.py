   
import unittest
from src.models.member import Member
from src.models.workout import Workout
from src.models.activity import Activity

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member(name="John", age=25, memb_type="Premium", memb_status=True)
        self.workout = Workout(name="MMA", capacity=15, prem_only=True)
        self.activity = Activity(self.workout, self.member)