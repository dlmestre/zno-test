import logging

from jsondownloader.requesthelper import Requests

log = logging.getLogger(__name__)


class Download:

    def __init__(self):
        self.session = Requests.session()

    def json(self, url):
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        log.error('Request {0} STATUS {1}'.format(response.url, response.status_code))
