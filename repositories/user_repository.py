from db.run_sql import run_sql

from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Save a user to the database
def save(user):
    sql = "INSERT INTO users (first_name, last_name, favorite_destination) VALUES (%s, %s, %s) RETURNING id"
    values = [user.first_name, user.last_name, user.favorite_destination]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

# Select all users
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['first_name'], row['last_name'], row['favorite_destination'], row['id'])
        users.append(user)
    return users

# Select a user by ID
def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['first_name'], result['last_name'], result['id'] )
    return user

# Delete all users
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

# Delete user by id
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)