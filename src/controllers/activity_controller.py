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
    for workout in workouts:
                fullness = len(workout_repository.members_in_class(workout))
                setattr(workout, "fullness", fullness)
    if member.memb_type == "Standard":
        only_standard = []
        for workout in workouts:
            if workout.prem_only == False:
                only_standard.append(workout)
        workouts = only_standard
    return render_template("activity/new.html", member = member, workout_dict = workouts)


@activities_blueprint.route("/activities/<id>", methods=["POST"])
def add_member_to_class_finish(id):
    member = member_repository.select(id)
    workout_id = request.form['workout_id']
    workout = workout_repository.select(workout_id)
    workout_name = workout_repository.select(workout_id).name
    all_activity = activity_repository.select_all()
    for activity in range(len(all_activity)):
        if all_activity[activity].member.id == member.id and all_activity[activity].workout.id == workout.id:
            workouts = workout_repository.select_all().copy()
            for workout in workouts:
                fullness = len(workout_repository.members_in_class(workout))
                setattr(workout, "fullness", fullness)
            if member.memb_type == "Standard":
                only_standard = []
                for workout in workouts:
                    if workout.prem_only == False:
                        only_standard.append(workout)
                workouts = only_standard
            return render_template("activity/error.html", member = member, workout_dict = workouts, workout_name = workout_name)
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
    for member in members:
        already_in = activity_repository.is_member_in_class(member.id, id)
        setattr(member, "already_in", already_in)
    return render_template("activity/add_members.html", workout = workout, member_list=members)

@activities_blueprint.route("/activities/add_members/<id>", methods=['POST'])
def add_members_finish(id):
    workout = workout_repository.select(id)
    to_be_added = []
    members = member_repository.select_all()
    chkbox_values = request.form.getlist('chkbox')
    len_of_to_be_added = len(chkbox_values)
    members_already_in_class = len(workout_repository.members_in_class(workout))
    free_space = workout.capacity - members_already_in_class
    if free_space+1 <= len_of_to_be_added:
        for member in members:
            already_in = activity_repository.is_member_in_class(member.id, id)
            setattr(member, "already_in", already_in)
        return render_template("activity/add_members_error.html", workout = workout, member_list=members, free_space=free_space, len_of_to_be_added=len_of_to_be_added )
    for member in chkbox_values:
        for y in members:
            if int(member) == int(y.id):
                to_be_added.append(y)
    for member in to_be_added:
        new_activity = Activity(workout, member)
        activity_repository.save(new_activity)
        new_activity = None
    return redirect(f"/activities/add_members/{id}")




