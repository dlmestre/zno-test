import os


class UrlException(Exception):
    pass

class Url:

    @staticmethod
    def stringify(url, *values):
        if not url:
            raise UrlException('URL not defined')
        return os.path.join(url, os.path.join(*[str(value) for value in values]))
