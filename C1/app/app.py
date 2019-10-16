import argparse
import os

from jsondownloader.download import Download
from storage.storage import Storage
from utils.parsedate import Date
from utils.url import Url


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date",  dest="date")
    parser.add_argument("-u", "--url",  dest="url")
    args = parser.parse_args()

    date = Date.parser(os.environ.get('DATE', args.date))
    url = Url.stringify(os.environ.get('URL', args.url), date.year, date.month, date.day)

    download = Download()

    with Storage(date) as storage:
        for hour in range(1, 25):
            storage.feed(hour, download.json(Url.stringify(url, hour)))

if __name__ == '__main__':
    main()
