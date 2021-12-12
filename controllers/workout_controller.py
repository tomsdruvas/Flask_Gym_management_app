from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
from models.workout import Workout
import repositories.activity_repository as activity_repository
import repositories.workout_repository as workout_repository
import repositories.workout_repository as workout_repository


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
    age = request.form["age"]
    memb_type = request.form["memb_type"]
    memb_status = True
    new_workout = Workout(name, age, memb_type, memb_status)
    workout_repository.save(new_workout)
    return redirect("/workouts")

@workouts_blueprint.route("/workouts/<id>", methods=['GET'])
def show_workout(id):
    workout = workout_repository.select(id)
    return render_template('workouts/show.html', workout = workout)



@workouts_blueprint.route("/workouts/<id>/edit", methods=['GET'])
def edit_workout(id):
    workout = workout_repository.select(id)
    memb_status = workout_repository.select(id).memb_status
    memb_type = workout_repository.select(id).memb_type
    return render_template('workouts/edit.html', workout = workout, memb_status = memb_status, memb_type=memb_type)

@workouts_blueprint.route("/workouts/<id>", methods=['POST'])
def update_workout(id):
    name = request.form['name']
    age = request.form['age']
    memb_type = request.form['memb_type']
    memb_status = True
    if request.form['memb_type'] == "Inactive":
        memb_status = False
        memb_type = workout_repository.select(id).memb_type
    workout = Workout(name, age, memb_type, memb_status, id)
    workout_repository.update(workout)
    return redirect('/workouts')


@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect('/workouts')


