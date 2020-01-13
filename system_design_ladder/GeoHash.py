class GeoHash:
    BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        lat_bin = self._get_bin(latitude, -90, 90)
        lon_bin = self._get_bin(longitude, -180, 180)
        merge_bin = ''
        for i in range(30):
            # longitude binary first
            merge_bin += lon_bin[i]
            merge_bin += lat_bin[i]

        encoded = ''
        for i in range(0, 60, 5):
            # get the string representation of binary form
            encoded += GeoHash.BASE32[int(merge_bin[i: i+5], 2)]
        return encoded[:precision]

    def _get_bin(self, val, low, high):
        binary = ''
        for i in range(30):  # 30 + 30 = 60 ==> 60 / 5 = 12 characters, enough precision
            mid = (low + high) / 2
            if val <= mid:
                binary += '0'
                high = mid
            else:
                binary += '1'
                low = mid
        return binary


if __name__ == '__main__':
    geoHash = GeoHash()
    geoHash.encode(39.92816697, 116.38954991, 12)