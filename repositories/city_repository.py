from db.run_sql import run_sql

from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Save a city to the database
def save(city):
    sql = "INSERT INTO cities (country_id, city_name) VALUES (%s, %s) RETURNING id"
    values = [city.country.id, city.city_name]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return city

# Select all cities
def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(country, row['city_name'], row['id'])
        cities.append(city)
    return cities

# Select a city by ID
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        city = City(country, result['city_name'], result['id'])
    return city

# Delete all cities
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

# Delete city by id
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)