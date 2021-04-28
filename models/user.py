class User:
    def __init__(self, first_name, last_name, favorite_destination, id = None):
      self.first_name = first_name
      self.last_name = last_name
      self.favorite_destination = favorite_destination
      self.id = id

    def worldly_score(self):
      num_of_dest = []
      for destination in destinations:
        if destination.user.id == user.id and destination.visited == True:
          num_of_dest += 1
      return (len(num_of_dest) / 195) * 100