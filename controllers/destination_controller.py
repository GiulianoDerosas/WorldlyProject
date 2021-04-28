from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations", __name__)

# Create an individual country page
@destinations_blueprint.route("/destinations/country/<id>")
def display_destination_country(id):
    user = user_repository.select_all()
    countries = country_repository.select(id)
    cities = city_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template(f'/destinations/country/{id}.html', user=user, countries=countries, cities=cities, destinations=destinations)

# Create an individual city page
@destinations_blueprint.route("/destinations/city/<id>")
def display_destination_city(id):
    user = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template(f'/destinations/city/{id}.html', user=user, countries=countries, cities=cities, destinations=destinations)