from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

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



# @members_blueprint.route("/members/<id>")
# def show(id):
#     member = member_repository.select(id)
#     workouts = member_repository.workouts(member)
#     return render_template("members/show.html", member=member, workouts=workouts)






