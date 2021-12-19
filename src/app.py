from flask import Flask, render_template
from controllers.workout_controller import workouts_blueprint
from controllers.member_controller import members_blueprint
from controllers.activity_controller import activities_blueprint
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository



app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(workouts_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)

@app.route('/')
def home():
    members = member_repository.select_all()
    member_count = len(members)
    premium_count = 0
    for member in members:
        if member.memb_type == "Premium":
            premium_count += 1
    classes = workout_repository.select_all()
    class_count = len(classes)
    workouts = workout_repository.select_all()
    fullness = 0
    for workout in range(len(workouts)):
        workout_id = workouts[workout]
        fullness += len(workout_repository.members_in_class(workout_id))
        total_space = 0
    for workout in workouts:
        total_space += workout_repository.select(workout.id).capacity
    total_prem_space = 0
    used_prem_space = 0
    for workout in workouts:
        if workout_repository.select(workout.id).prem_only == True:
            total_prem_space += workout_repository.select(workout.id).capacity
            used_prem_space += len(workout_repository.members_in_class(workout))
    return render_template('index.html', member_count = member_count, premium_count = premium_count, class_count=class_count, fullness = fullness, total_space = total_space, total_prem_space = total_prem_space, used_prem_space=used_prem_space)



@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404



if __name__ == '__main__':
    app.run(debug=True)
