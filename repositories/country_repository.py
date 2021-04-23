from db.run_sql import run_sql

from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Save a country to the database
def save(country):
    sql = "INSERT INTO countries (country_name) VALUES (%s) RETURNING id"
    values = [country.country_name]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return country

# Select all countries
def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['country_name'], row['id'])
        countries.append(country)
    return countries

# Select a country by ID
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['country_name'], result['id'])
    return country

# Delete all countries
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

# Delete country by id
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)