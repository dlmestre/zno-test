import ssl

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

ssl._create_default_https_context = ssl._create_unverified_context


class Requests:

    @staticmethod
    def session(retries=3, backoff_factor=1, status_forcelist=(502, 503, 504)):
        session = Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
