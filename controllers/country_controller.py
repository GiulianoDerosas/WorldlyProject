from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

countries_blueprint = Blueprint("countries", __name__)

@cities_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("country/index.html", countries = countries)