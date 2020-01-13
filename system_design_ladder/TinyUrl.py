import string
import math

class TinyUrl:
    BASE62 = string.ascii_letters + string.digits
    RANGE = int(math.pow(62, 6))
    DOMAIN = "http://tiny.url/"

    def __init__(self):
        self.code_to_url = {}

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        code = self._to_integer(url)
        short_url = self._encode(code)
        self.code_to_url[code] = url
        return TinyUrl.DOMAIN + short_url

    def _to_integer(self, url):
        ans = 0
        for a in url:
            ans = (ans * 31 + ord(a)) % TinyUrl.RANGE
        while ans in self.code_to_url and self.code_to_url[ans] != url:
            ans = (ans + 1) % TinyUrl.RANGE
        return ans

    def _encode(self, code):
        short = ''
        while code > 0:
            # it is easier to under from prepend because it is "easier" to decode it
            short = TinyUrl.BASE62[code % 62] + short
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
            ans = ans * 62 + TinyUrl.BASE62.index(c)
        return ans


if __name__ == '__main__':
    tinyUrl = TinyUrl()
    print(tinyUrl.shortToLong(tinyUrl.longToShort("http://www.lintcode.com/faq/?id=10")))