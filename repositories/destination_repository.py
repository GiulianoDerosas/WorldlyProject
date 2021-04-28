from db.run_sql import run_sql

import pdb
from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# Save a destination to the database
def save(destination):
    sql = "INSERT INTO destinations (user_id, country_id, city_id, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [destination.user.id, destination.country.id, destination.city.id, destination.visited]
    results = run_sql(sql, values)
    destination.id = results[0]['id']
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
        destination = Destination(user, country, city, row['visited'], row['id'])
        destinations.append(destination)
    return destinations

# Select a destination by ID
def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = user_repository.select(result['user_id'])
        country = country_repository.select(result['country_id'])
        city = city_repository.select(result['city_id'])
        destination = Destination(user, country, city, result['visited'], result['id'])
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

# Update the destination
def update(destination):
    sql = "UPDATE destinations SET (user_id, country_id, city_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [destination.user.id, destination.country.id, destination.city.id, destination.visited, destination.id]
    run_sql(sql, values)

def worldly_score(user_id):
    destinations = select_all()
    num_of_dest = 0
    for destination in destinations:
        if destination.visited == True and destination.user.id == int(user_id):
            num_of_dest += 1
    return round((num_of_dest / 195) * 100, 2)
