from flask import Flask, render_template, request, redirect

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)