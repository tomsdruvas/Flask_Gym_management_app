from flask import Flask, render_template, request, redirect
from flask import Blueprint
from src.controllers.member_controller import members
from src.models.activity import Activity
from src.models.workout import Workout
import src.repositories.activity_repository as activity_repository
import src.repositories.workout_repository as workout_repository
import src.repositories.workout_repository as workout_repository


workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/workouts")
def workouts():
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", workouts = workouts)

@workouts_blueprint.route("/workouts/new")
def new_workout():
    return render_template("workouts/new.html")

@workouts_blueprint.route("/workouts", methods=["POST"])
def create_workout():
    name = request.form["name"]
    capacity = request.form["capacity"]
    prem_required = request.form["prem_required"]    
    new_workout = Workout(name, capacity, prem_required)
    workout_repository.save(new_workout)
    return redirect("/workouts")

@workouts_blueprint.route("/workouts/<id>", methods=['GET'])
def show_workout(id):
    workout = workout_repository.select(id)
    current_participants = len(workout_repository.members_in_class(workout))
    members_going = workout_repository.members_in_class(workout)
    return render_template('workouts/show.html', workout = workout, members_going = members_going, current_participants = current_participants)



@workouts_blueprint.route("/workouts/<id>/edit", methods=['GET'])
def edit_workout(id):
    workout = workout_repository.select(id)
    prem_only = workout_repository.select(id).prem_only
    return render_template('workouts/edit.html', workout = workout, prem_only = prem_only)

@workouts_blueprint.route("/workouts/<id>", methods=['POST'])
def update_workout(id):
    name = request.form['name']
    capacity = request.form['capacity']
    prem_only = request.form['prem_only']
    workout = Workout(name, capacity, prem_only, id)
    workout_repository.update(workout)
    return redirect('/workouts')


@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect('/workouts')


