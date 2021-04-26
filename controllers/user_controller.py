from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.destination import Destination
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

users_blueprint = Blueprint("users", __name__)

# Get requests for /users route
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template("users/index.html", users=users, countries=countries, cities=cities, destinations=destinations)

# Creates a new user
@users_blueprint.route("/users", methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    favorite_destination = request.form['favorite_destination']
    user = User(first_name, last_name, favorite_destination)
    user_repository.save(user)
    return redirect('/users')

# Create an individual profile page 
@users_blueprint.route("/users/<id>")
def display_user_profile(id):
    user = user_repository.select(id)
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template("/users/profile.html", user=user, countries=countries, cities=cities, destinations=destinations)

# Creates a new destination
@users_blueprint.route("/users/<id>", methods=['POST'])
def create_destination(id):
    user_id = id
    country_id = request.form['countries']
    city_id = request.form['cities']

    user = user_repository.select(id)
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)

    destination = Destination(user, country, city)
    destination_repository.save(destination)
    return redirect(f'/users/{id}')
