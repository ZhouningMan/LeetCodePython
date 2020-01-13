class GeoHash:
    BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        binary = self._to_bin(geohash)
        lon_bin = [binary[i] for i in range(0, len(binary), 2)]
        lat_bin = [binary[i] for i in range(1, len(binary), 2)]

        longitude = self._bin_to_val(-180, 180, lon_bin)
        latitude = self._bin_to_val(-90, 90, lat_bin)
        return latitude, longitude

    def _to_bin(self, geohash):
        binary = ''
        for c in geohash:
            idx = GeoHash.BASE32.index(c)
            b = ''
            for i in range(5):
                b = str(idx % 2) + b
                idx = idx // 2
            binary += b
        return binary

    def _bin_to_val(self, low, high, binary):
        for b in binary:
            mid = (high + low) / 2
            if b == '1':  # our value is higher
                low = mid
            else:  # our value is lower
                high = mid
        return (low + high) / 2

if __name__ == '__main__':
    geoHash = GeoHash()
    geoHash.decode("wx4g0s")
