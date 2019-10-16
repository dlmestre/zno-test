import os

import pandas as pd
from pandas.io.json import json_normalize


class CSVException(Exception):
    pass

class Storage:

    name = 'export.csv'

    def __enter__(self):
        self.dataframes = []
        return self

    def __init__(self, date):
        self.directory = os.path.join(str(date.year), str(date.month), str(date.day))

    def feed(self, hour, jsondata):
        if jsondata:
            df = json_normalize(jsondata)
            df['hour'] = hour
            self.dataframes.append(df)

    def __exit__(self, *args):
        if not self.dataframes:
            raise CSVException('No data found on the url provided')
        df = pd.concat(self.dataframes, ignore_index=True)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        df.to_csv(os.path.join(self.directory, self.name))
