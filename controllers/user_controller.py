from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)


# @users_blueprint.route("/",  methods=['POST'])
# def create_user():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')