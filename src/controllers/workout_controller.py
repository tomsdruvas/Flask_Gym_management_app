from flask import Flask, render_template, request, redirect
import datetime
from flask import Blueprint
from controllers.member_controller import members
from models.activity import Activity
from models.workout import Workout
import repositories.activity_repository as activity_repository
import repositories.workout_repository as workout_repository
import repositories.workout_repository as workout_repository


workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/workouts")
def workouts():
    workouts = workout_repository.select_all()
    for workout in workouts:
        datetime_object = str(workout.class_time)
        x = datetime.datetime.strptime(datetime_object, "%Y-%m-%d %H:%M:%S")
        display_class_time = x.strftime("%a, %d. %b %H:%M")
        setattr(workout, "display_class_time", display_class_time)
    return render_template("workouts/index.html", workouts = workouts)

@workouts_blueprint.route("/workouts/new")
def new_workout():
    return render_template("workouts/new.html")

@workouts_blueprint.route("/workouts", methods=["POST"])
def create_workout():
    name = request.form["name"]
    capacity = request.form["capacity"]
    prem_only = request.form["prem_only"]
    class_time = request.form["class_time"]
    new_workout = Workout(name, capacity, prem_only, class_time)
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
    # Converting the times
    x = datetime.datetime.strptime(str(workout.class_time), "%Y-%m-%d %H:%M:%S")
    display_class_time = x.strftime("%Y-%m-%dT%H:%M")
    pre_display_time = display_class_time
    return render_template('workouts/edit.html', workout = workout, prem_only = prem_only, pre_display_time=pre_display_time)

@workouts_blueprint.route("/workouts/<id>", methods=['POST'])
def update_workout(id):
    name = request.form['name']
    capacity = request.form['capacity']
    prem_only = request.form['prem_only']
    class_time = request.form["class_time"]
    workout = Workout(name, capacity, prem_only, class_time, id)
    workout_repository.update(workout)
    return redirect('/workouts')


@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect('/workouts')

@workouts_blueprint.route("/workouts/calendar")
def calendar_view():
    return render_template("workouts/calendar/index.html")


