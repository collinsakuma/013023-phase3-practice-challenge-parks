
class Trip:
    all = []

    def __init__(self, visitor, nation_park, start_date, end_date):
        self.visitor = visitor
        self.nation_park = nation_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    
