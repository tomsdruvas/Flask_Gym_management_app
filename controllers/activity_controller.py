import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


activities_blueprint = Blueprint("activities", __name__)



@activities_blueprint.route("/activities/<id>")
def activities(id):
    member = member_repository.select(id)
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
    if member.memb_type == "Standard":
        only_standard = []
        for workout in workout_dict:
            if workout["prem_only"] == True:
                only_standard.append(workout)
        workout_dict = only_standard
    return render_template("activity/new.html", member = member, workout_dict = workout_dict)


@activities_blueprint.route("/activities/<id>", methods=["POST"])
def add_member_to_class_finish(id):
    workout_id = request.form['workout_id']
    workout = workout_repository.select(workout_id)
    member = member_repository.select(id)
    all_activity = activity_repository.select_all()
    for activity in range(len(all_activity)):
        if all_activity[activity].member.id == member.id and all_activity[activity].workout.id == workout.id:
            return render_template("activity/error.html")

    new_activity = Activity(workout, member)
    activity_repository.save(new_activity)
    return redirect(f"/members/{id}")