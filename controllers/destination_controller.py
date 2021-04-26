from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations", __name__)

