class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        pass


class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        pass


class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        pass


class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethod
    def encode(cls, location):
        pass

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        pass