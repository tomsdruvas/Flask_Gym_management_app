from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.activity import Activity
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.activity_repository as activity_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    age = request.form["age"]
    memb_type = request.form["memb_type"]
    memb_status = True
    new_member = Member(name, age, memb_type, memb_status)
    member_repository.save(new_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
    member = member_repository.select(id)
    active_classes = member_repository.workouts(member)
    return render_template('members/show.html', member = member, active_classes = active_classes)



@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    memb_status = member_repository.select(id).memb_status
    memb_type = member_repository.select(id).memb_type
    return render_template('members/edit.html', member = member, memb_status = memb_status, memb_type=memb_type)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    age = request.form['age']
    memb_type = request.form['memb_type']
    memb_status = True
    if request.form['memb_type'] == "Inactive":
        memb_status = False
        memb_type = member_repository.select(id).memb_type
    member = Member(name, age, memb_type, memb_status, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')


# @members_blueprint.route("/members/activities", methods=["POST"])
# def add_member_to_class_finish(id):
#     workout = request.form['workout_id']
#     member = member_repository.select(id).id
#     new_activity = Activity(workout, member)
#     activity_repository.save(new_activity)
#     return redirect("/members/<id>/activities")


