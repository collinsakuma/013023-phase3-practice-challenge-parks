from .trip import Trip

class Visitor:

    def __init__(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else: 
            print("name cannot be changed!")

    def trips(self):
        trips_list = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips_list.append(trip)
        return trips_list

    def nationalparks(self):
        park_list = []
        for trip in self.trips():
            if trip.nation_park not in park_list:
                park_list.append(trip.nation_park)
        return park_list

    def create_trip(self, nation_park, start_date, end_date):
        return Trip(self, nation_park, start_date, end_date)