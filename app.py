from flask import Flask, render_template

from controllers.workout_controller import workouts_blueprint
from controllers.member_controller import members_blueprint
from controllers.activity_controller import activities_blueprint
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


app = Flask(__name__)

app.register_blueprint(workouts_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)

@app.route('/')
def home():
    members = member_repository.select_all()
    member_count = len(members)
    premium_count = 0
    for member in members:
        if member.memb_type == True:
            premium_count += 1
    return render_template('index.html', member_count = member_count)

if __name__ == '__main__':
    app.run(debug=True)