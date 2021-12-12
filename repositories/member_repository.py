from db.run_sql import run_sql
from models.member import Member
from models.workout import Workout

def save(member):
    sql = "INSERT INTO members( name, age, memb_type, memb_status ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.name, member.age, member.memb_type, member.memb_status]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member


def update(member):
    sql = "UPDATE members SET ( name, age, memb_type, memb_status ) = ( %s, %s, %s, %s ) WHERE id = %s"
    values = [member.name, member.age, member.memb_type, member.memb_status, member.id]
    print(values)
    run_sql(sql, values)

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['age'], row['memb_type'], row['memb_status'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['age'], result['memb_type'], result['memb_status'], result['id'] )
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def workouts(member):
    workouts = []
    sql = "SELECT workouts.* FROM workouts \
            INNER JOIN activities \
            ON activities.workout_id = workouts.id \
            WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        workout = Workout(row['name'], row['capacity'], row['prem_only'], row['id'])
        workouts.append(workout)
    return workouts



