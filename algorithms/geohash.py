# Demonstration for Mr. Gopi after our discussion on 2020-06-14
# Used PEP8 convention as much as possible

from json import load
from statistics import mean


class GeoHash():
    geo_hash_dict = load(open('geohash_alphabet.json', 'r'))
    lat_range = [-90, 90]
    long_range = [-180, 180]

    @staticmethod
    def lat_long_decoder(lat_long_code, lat_long_range):
        for i in lat_long_code:
            if i == '0':
                lat_long_range[1] = mean(lat_long_range)
            elif i == '1':
                lat_long_range[0] = mean(lat_long_range)
        return mean(lat_long_range)

    def geo_hash_to_decimal(self, geo_hash_string: str) -> [str, int]:
        decimal = 0
        for i in range(0, len(geo_hash_string)):
            decimal += (32 ** i) * self.geo_hash_dict[0][geo_hash_string[-i - 1]]
        return [geo_hash_string, decimal]

    def geo_hash_to_lat_log(self, geo_hash_string: str) -> [float, float]:
        lat_long_string = ""
        for i in geo_hash_string:
            lat_long_string += self.geo_hash_dict[1][str(self.geo_hash_dict[0][i])]
        long_code = lat_long_string[0::2]
        lat_code = lat_long_string[1::2]
        return [self.lat_long_decoder(lat_code, self.lat_range), self.lat_long_decoder(long_code, self.long_range)]

    def decimal_to_geo_hash(self):
        pass


if __name__ == '__main__':
    geo_hash = GeoHash()
    print(geo_hash.geo_hash_to_lat_log('ezs42'))
