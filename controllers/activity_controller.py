from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


activities_blueprint = Blueprint("activities", __name__)



@activities_blueprint.route("/activities/<id>")
def activities(id):
    member = member_repository.select(id)
    workouts = workout_repository.select_all()
    return render_template("activity/new.html", member = member, workouts = workouts)


@activities_blueprint.route("/activities/<id>", methods=["POST"])
def add_member_to_class_finish(id):
    workout_id = request.form['workout_id']
    workout = workout_repository.select(workout_id)
    member = member_repository.select(id)
    new_activity = Activity(workout, member)
    activity_repository.save(new_activity)
    return redirect("/members")