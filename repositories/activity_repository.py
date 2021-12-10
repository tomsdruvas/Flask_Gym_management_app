from db.run_sql import run_sql
from models.activity import Activity
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

def save(activity):
    sql = "INSERT INTO activities ( workout_id, member_id ) VALUES ( %s, %s) RETURNING id"
    values = [activity.workout.id, activity.member.id]
    results = run_sql( sql, values )
    activity.id = results[0]['id']
    return activity


def select_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        activity = Activity(workout, member, row['id'])
        activities.append(activity)
    return activities


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
