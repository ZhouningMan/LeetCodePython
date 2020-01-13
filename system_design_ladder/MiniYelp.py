from .Helper.YelpHelper import Location, Restaurant, GeoHash, Helper

class TrieNode:
    def __init__(self, c, restaurant = None):
        self.c = c
        self.children = [None] * 128 # only need to 32
        self.restaurant = restaurant

class MiniYelp:
    ERRORS = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]

    def __init__(self):
        self.id_to_restaurant = {}
        self.trie = TrieNode(None)  # trie root

    def _add_to_trie(self, trie, i, geo_hash, restaurant):
        if i == len(geo_hash):
            return
        node = trie.children[ord(geo_hash[i])]
        if node is None:
            node = TrieNode(ord(geo_hash[i]))
            trie.children[ord(geo_hash[i])] = node

        if i == len(geo_hash) - 1:
            node.restaurant = restaurant
            return
        self._add_to_trie(node, i + 1, geo_hash, restaurant)

    # we might have a lot of orphan nodes, improve this
    def _remove_from_trie(self, node, geo_hash, i):
        if not node:
            return
        if i == len(geo_hash): # found the target node
            node.restaurant = None
            return
        self._remove_from_trie(node.children[ord(geo_hash[i])], geo_hash, i + 1)

    def _collect(self, result, trie, prefix, i):
        if trie is None:
            return
        if i < len(prefix):
            self._collect(result, trie.children[ord(prefix[i])], prefix, i + 1)
            return
        if trie.restaurant:
            result.append(trie.restaurant)
        for child in trie.children:
            self._collect(result, child, prefix, i)

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        geo_hash = GeoHash.encode(location)
        restaurant = Restaurant.create(name, location)
        self.id_to_restaurant[restaurant.id] = restaurant
        self._add_to_trie(self.trie, 0, geo_hash, restaurant)
        return restaurant.id

    def remove_restaurant(self, restaurant_id):
        restaurant = self.id_to_restaurant.pop(restaurant_id)
        geo_hash = GeoHash.encode(restaurant.location)
        self.id_to_restaurant.pop(restaurant_id)
        self._remove_from_trie(self.trie, geo_hash, 0)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        geo_hash = GeoHash.encode(location)
        length = self._get_length(k)
        prefix = geo_hash[:length]  # we get the ceiling
        restaurants = []
        self._collect(restaurants, self.trie, prefix, 0)
        pairs = []
        for res in restaurants:
            dist = Helper.get_distance(res.location, location)
            if dist <= k:
                pairs.append((res, dist))

        pairs = sorted(pairs, key=lambda r: r[1])
        return [r[0].name for r in pairs]

    def _get_length(self, k):
        length = len(MiniYelp.ERRORS)
        for i in range(length):
            if k > MiniYelp.ERRORS[i]:
                return i
        return length
