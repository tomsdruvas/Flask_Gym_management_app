import pdb

from models.workout import Workout
from models.activity import Activity
from models.member import Member

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


# activity_repository.delete_all()
# workout_repository.delete_all()
# member_repository.delete_all()


# member1 = Member("John", 20, "Premium", True)
# member2 = Member("Paul", 25, "Standard", True)
# workout1 = Workout("HIIT", 10, True)
# workout2 = Workout("Cardio and weight", 12, False, 2)
# member_repository.save(member1)
# member_repository.save(member2)
# workout_repository.save(workout1)
# workout_repository.update(workout2)


# results = member_repository.select_all()
# for member in results:
#     print(member.__dict__)

# results = workout_repository.select_all()
# for workout in results:
#     print(workout.__dict__)



# activity1 = Activity(workout1, member1)
# activity2 = Activity(workout2, member2)

# activity_repository.save(activity1)
# activity_repository.save(activity2)


# results = activity_repository.select_all()
# for activity in results:
#     print(activity)



# member3 = Member("Duncan", 23, "Standard", True)
# member_repository.save(member3)

# member_repository.delete(17)

workouts = workout_repository.select_all()
workout_dict = []
new_dict = {}
for workout in range(len(workouts)):
    workout_id = workouts[workout]
    fullness = len(workout_repository.members_in_class(workout_id))
    new_dict["fullness"] = fullness
    new_dict["name"] = workout_repository.select(workout_id.id).name
    new_dict["capacity"] = workout_repository.select(workout_id.id).capacity
    new_dict["prem_only"] = workout_repository.select(workout_id.id).prem_only
    new_dict["id"] = workout_repository.select(workout_id.id).id
    workout_dict.append(new_dict)
    new_dict = {}
    # print(workout_dict)


only_standard = []
for workout in workout_dict:
    if workout["prem_only"] == True:
        only_standard.append(workout)
print(only_standard)


    


# for workout in workouts:
#     print(len(workout_repository.members_in_class(workout)))
# print(workout_dict)

# workout_dict = workouts
#     # for x in workout_dict:
#     #     workout_repository.members_in_class(x)
#     #     x["fullness"] = 