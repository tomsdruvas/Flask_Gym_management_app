from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member

def save(workout):
    sql = "INSERT INTO workouts(name, capacity) VALUES ( %s, %s ) RETURNING id"
    values = [workout.name, workout.capacity]
    results = run_sql( sql, values )
    workout.id = results[0]['id']
    return workout


def select_all():
    workouts = []

    sql = "SELECT * FROM workouts"
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['capacity'], row['id'])
        workouts.append(workout)
    return workouts


def select(id):
    workout = None
    sql = "SELECT * FROM workouts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        workout = Workout(result['name'], result['capacity'], result['id'] )
    return workout


def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)


def members_in_class(workout):
    members = []
    sql ="SELECT members.* FROM members \
            INNER JOIN activities \
            ON activities.member_id = members.id \
            WHERE workout_id = %s"
    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['age'], row['memb_type'], row['memb_status'], row['id'])
        members.append(member)
    return members
    



