import src.repositories.member_repository as member_repository
import src.repositories.workout_repository as workout_repository

class Activity:
    def __init__(self, workout, member, id = None):
        self.workout = workout
        self.member = member
        self.id = id


def is_member_in_class(member_id, workout_id):
    workout = workout_repository.select(workout_id)
    members = workout_repository.members_in_class(workout)
    for member in members:
        if member.id == member_id:
            return True
    return False