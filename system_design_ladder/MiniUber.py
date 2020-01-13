from system_design_ladder.Helper.Trip import Trip, Helper

class MiniUber:

    def __init__(self):
        self.driverToLoc = {}
        self.driverToTrip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        self.driverToLoc[driver_id] = (lat, lng)
        return self.driverToTrip.get(driver_id, None)

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        dist = -1
        closet_dr = -1
        for driver, loc in self.driverToLoc.items():
            if driver in self.driverToTrip:
                continue
            d = Helper.get_distance(lat, lng, loc[0], loc[1])
            if closet_dr == -1 or d < dist:
                closet_dr = driver
                dist = d
        if closet_dr == -1:
            return None

        trip = Trip(rider_id, lat, lng)
        trip.driver_id = closet_dr
        self.driverToTrip[closet_dr] = trip
        return trip