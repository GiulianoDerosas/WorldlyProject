from flask import Flask, render_template, request, redirect

from models.user import User
from models.destination import Destination
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.destination_repository as destination_repository

from controllers.user_controller import users_blueprint
from controllers.destination_controller import destinations_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(destinations_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# def worldly_score():
#       num_of_dest = []
#       destination_repository.select_all()
#       user_repository.select_all()
#       for destination in destinations:
#         if destination.user.id == user.id and destination.visited == True:
#           num_of_dest += 1
#       return (len(num_of_dest) / 195) * 100

# app.jinja_env.globals.update(worldly_score=worldly_score)



if __name__ == '__main__':
    app.run(debug=True)