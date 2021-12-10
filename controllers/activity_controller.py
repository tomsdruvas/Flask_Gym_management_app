from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


activities_blueprint = Blueprint("activities", __name__)