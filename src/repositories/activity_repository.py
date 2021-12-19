from src.db.run_sql import run_sql
from src.models.activity import Activity
import src.repositories.member_repository as member_repository
import src.repositories.workout_repository as workout_repository

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

def is_member_in_class(member_id, workout_id):
    workout = workout_repository.select(workout_id)
    members = workout_repository.members_in_class(workout)
    for member in members:
        if member.id == member_id:
            return True
    return False

