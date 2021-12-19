import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from src.models.activity import Activity
from src.db.run_sql import run_sql
from src.models.workout import Workout
from src.models.member import Member
import src.repositories.activity_repository as activity_repository
import src.repositories.member_repository as member_repository
import src.repositories.workout_repository as workout_repository


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
            if workout["prem_only"] == False:
                only_standard.append(workout)
        workout_dict = only_standard
    return render_template("activity/new.html", member = member, workout_dict = workout_dict)


@activities_blueprint.route("/activities/<id>", methods=["POST"])
def add_member_to_class_finish(id):
    member = member_repository.select(id)
    workout_id = request.form['workout_id']
    workout = workout_repository.select(workout_id)
    workout_name = workout_repository.select(workout_id).name
    all_activity = activity_repository.select_all()
    for activity in range(len(all_activity)):
        if all_activity[activity].member.id == member.id and all_activity[activity].workout.id == workout.id:
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
                    if workout["prem_only"] == False:
                        only_standard.append(workout)
                workout_dict = only_standard
            return render_template("activity/error.html", member = member, workout_dict = workout_dict, workout_name = workout_name)
    new_activity = Activity(workout, member)
    activity_repository.save(new_activity)
    return redirect(f"/members/{id}")

@activities_blueprint.route("/activities/<id>/delete/member", methods=['POST'])
def delete_member_from_class(id):
    member_id = request.form['member']
    member = member_repository.select(member_id)
    workout = workout_repository.select(id)
    all_activity = activity_repository.select_all()
    to_delete = None
    for activity in range(len(all_activity)):
        if all_activity[activity].member.id == member.id and all_activity[activity].workout.id == workout.id:
            to_delete = all_activity[activity].id

    activity_repository.delete(to_delete)
    return redirect(f"/workouts/{id}")


@activities_blueprint.route("/activities/<id>/delete/class", methods=['POST'])
def delete_class_from_member(id):
    workout_id = request.form['workout']
    workout = workout_repository.select(workout_id)
    member = member_repository.select(id)
    all_activity = activity_repository.select_all()
    to_delete = None
    for activity in range(len(all_activity)):
        if all_activity[activity].member.id == member.id and all_activity[activity].workout.id == workout.id:
            to_delete = all_activity[activity].id

    activity_repository.delete(to_delete)
    return redirect(f"/members/{id}")

@activities_blueprint.route("/activities/add_members/<id>")
def add_members(id):
    workout = workout_repository.select(id)
    members = member_repository.select_all()
    member_list = []
    new_dict = {}
    for member in range(len(members)):
        member_id = members[member]
        already_in = activity_repository.is_member_in_class(member_id.id, id)
        new_dict["already_in"] = already_in
        new_dict["name"] = member_repository.select(member_id.id).name
        new_dict["age"] = member_repository.select(member_id.id).age
        new_dict["memb_type"] = member_repository.select(member_id.id).memb_type
        new_dict["memb_status"] = member_repository.select(member_id.id).memb_status
        new_dict["id"] = member_repository.select(member_id.id).id
        member_list.append(new_dict)
        new_dict = {}
    return render_template("activity/add_members.html", workout = workout, member_list=member_list)

@activities_blueprint.route("/activities/add_members/<id>", methods=['POST'])
def add_members_finish(id):
    workout = workout_repository.select(id)
    to_be_added = []
    members = member_repository.select_all()
    chkbox_values = request.form.getlist('chkbox')
    for member in chkbox_values:
        for y in members:
            if int(member) == int(y.id):
                to_be_added.append(y)
    for member in to_be_added:
        new_activity = Activity(workout, member)
        activity_repository.save(new_activity)
        new_activity = None
    return redirect(f"/activities/add_members/{id}")




