import string
import math

class TinyUrl2:
    BASE62 = string.ascii_letters + string.digits
    RANGE = int(math.pow(62, 6))
    DOMAIN = "http://tiny.url/"

    def __init__(self):
        self.code_to_url = {}

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        if len(key) < 6:
            return "error"
        code = self._decode(key)
        if code in self.code_to_url and self.code_to_url[code] != long_url:
            return "error"
        self.code_to_url[code] = long_url
        return TinyUrl2.DOMAIN + key

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        code = self._to_integer(url)
        short_url = self._encode(code)
        self.code_to_url[code] = url
        return TinyUrl2.DOMAIN + short_url

    def _to_integer(self, url):
        ans = 0
        for a in url:
            ans = (ans * 31 + ord(a)) % TinyUrl2.RANGE
        while ans in self.code_to_url and self.code_to_url[ans] != url:
            ans = (ans + 1) % TinyUrl2.RANGE
        return ans

    def _encode(self, code):
        short = ''
        while code > 0:
            # it is easier to under from prepend because it is "easier" to decode it
            short = TinyUrl2.BASE62[code % 62] + short
            code //= 62
        while len(short) < 6:
            short = 'a' + short
        return short

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        code = self._decode(url[-6:])
        return self.code_to_url[code]

    def _decode(self, url):
        ans = 0
        for c in url:
            # in the encdoe we preprend 'a', but we have no problem because a is
            # the first character of our base62 string
            ans = ans * 62 + TinyUrl2.BASE62.index(c)
        return ans


if __name__ == '__main__':
    second = TinyUrl2()
    print(second.createCustom("http://www.lintcode.com/", "lccode"))
    print(second.longToShort("http://www.lintcode.com/problem/"))
    print(second.shortToLong("http://tiny.url/lccode"))
    print(second.createCustom("http://www.lintcode.com/", "lc"))
    print(second.createCustom("http://www.lintcode.com/en/ladder/", "lccode"))