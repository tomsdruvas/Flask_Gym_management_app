import pdb

from models.workout import Workout
from models.activity import Activity
from models.member import Member
import datetime

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

# # member_repository.delete(17)

# workouts = workout_repository.select_all()
# workout_dict = []
# new_dict = {}
# for workout in range(len(workouts)):
#     workout_id = workouts[workout]
#     fullness = len(workout_repository.members_in_class(workout_id))
#     new_dict["fullness"] = fullness
#     new_dict["name"] = workout_repository.select(workout_id.id).name
#     new_dict["capacity"] = workout_repository.select(workout_id.id).capacity
#     new_dict["prem_only"] = workout_repository.select(workout_id.id).prem_only
#     new_dict["id"] = workout_repository.select(workout_id.id).id
#     workout_dict.append(new_dict)
#     new_dict = {}
#     # print(workout_dict)


# only_standard = []
# for workout in workout_dict:
#     if workout["prem_only"] == True:
#         only_standard.append(workout)
# print(only_standard)


# workout = 2
# member = 7
# all_activity = activity_repository.select_all()
# print(all_activity[0].id)

# for activity in range(len(all_activity)):
#     print(all_activity[activity].member.name)



# for activity in range(len(all_activity)):
#     if all_activity[activity].member.id == member and all_activity[activity].workout.id == workout:
#         print(all_activity[activity].id)


# workouts = workout_repository.select_all()
# fullness = 0
# for workout in range(len(workouts)):
#     workout_id = workouts[workout]
#     fullness += len(workout_repository.members_in_class(workout_id))
# print(fullness)

# workouts = workout_repository.select_all()
# total_space = 0
# for workout in workouts:
# #     total_space += workout_repository.select(workout.id).capacity
# workouts = workout_repository.select_all()
# total_prem_space = 0
# used_prem_space = 0
# for workout in workouts:
#     if workout_repository.select(workout.id).prem_only == True:
#         total_prem_space += workout_repository.select(workout.id).capacity
#         used_prem_space += len(workout_repository.members_in_class(workout))


# print(total_prem_space, used_prem_space)

# def is_member_in_class(member_id, workout_id):
#     workout = workout_repository.select(workout_id)
#     members = workout_repository.members_in_class(workout)
#     for member in members:
#         if member.id == member_id:
#             return True
#     return False

# print(workout_repository.members_in_class(2))

# print(is_member_in_class(12, 2))






# if member.memb_type == "Standard":
#     only_standard = []
#     for workout in workout_dict:
#         if workout["prem_only"] == False:
#             only_standard.append(workout)
#     workout_dict = only_standard




# for workout in workouts:
#     print(len(workout_repository.members_in_class(workout)))
# print(workout_dict)

# workout_dict = workouts
#     # for x in workout_dict:
#     #     workout_repository.members_in_class(x)
#     #     x["fullness"] = 

workouts = workout_repository.select_all()
for workout in workouts:
    datetime_object = str(workout.class_time)
    x = datetime.datetime.strptime(datetime_object, "%Y-%m-%d %H:%M:%S")
    display_class_time = x.strftime("%a, %d. %b %H:%M")
    setattr(workout, "display_class_time", display_class_time)
    

