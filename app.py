from flask import Flask, render_template, request, redirect

from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint
from controllers.user_controller import users_blueprint
from controllers.destination_controller import destinations_blueprint

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(destinations_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    favorite_destination = request.form['favorite_destination']
    user = User(first_name, last_name, favorite_destination)
    user_repository.save(user)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)