import pdb
from models.city import City
from models.country import Country
from models.user import User
from models.destination import Destination

user_1 = User('Giuliano', 'Derosas', 'Bali')
user_repository.save(user_1)

country_1 = Country('Thailand')
country_repository.save(country_1)

city_1 = City(country_1, 'Bangkok')
city_repository.save(city_1)

destination_1 = Destination(user_1, country_1, city_1, 'Street Food')
destination_repository.save(destination_1)