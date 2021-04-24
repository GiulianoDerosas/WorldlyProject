from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.destination import Destination
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template("users/index.html", users=users, countries=countries, cities=cities, destinations=destinations)

@users_blueprint.route("/users", methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    favorite_destination = request.form['favorite_destination']
    user = User(first_name, last_name, favorite_destination)
    user_repository.save(user)
    return redirect('/users')

@users_blueprint.route("/users/<id>")
def display_user_profile(id):
    user = user_repository.select(id)
    return render_template("users/profile.html", user=user)

@users_blueprint.route("/users<id>",  methods=['POST'])
def create_bucket_list_entry():
    country_id = request.form['country_id']
    city_id = request.form['city_id']
    visited = request.form['visited']
    user = user_repository.select(user_id)
    new_entry = Destination(user, location, review)
    destination_repository.save(new_entry)
    return redirect('/visits')