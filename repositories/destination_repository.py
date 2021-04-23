from db.run_sql import run_sql

from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Save a destination to the database
def save(destination):
    sql = "INSERT INTO destinations (user_id, country_id, city_id, favorite_thing) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [destination.user.id, destination.country.id, destination.city.id, destination.favorite_thing]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return destination

# Select all destinations
def select_all():
    destinations = []
    sql = "SELECT * FROM destinations"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['user_id'])
        country = country_repository.select(row['country_id'])
        city = city_repository.select(row['city_id'])
        destination = Destination(user, country, city, row['favorite_thing'], row['id'])
        destinations.append(destination)
    return destinations

# Select a destination by ID
def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        destination = Destination(user, country, city, row['favorite_thing'], row['id'])
    return destination

# Delete all destinations
def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

# Delete destination by id
def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)