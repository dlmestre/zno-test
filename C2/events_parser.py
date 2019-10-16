import pandas as pd
# requirements.txt -> pandas==0.23.4


def main():
    df = pd.read_csv('Events.csv')

    diff = df['timestamp'].apply(lambda x: pd.to_datetime(x)) # Converts date string into a python date type
    diff = diff.diff(1).dropna().reset_index(drop=True) # Drops NAN values and removes the indexes
    diff = diff.apply(lambda x: pd.Timedelta(x).total_seconds())
    df.drop(df.tail(1).index, inplace=True) # Removes last row in the dataframe
    df['ReadTime_sec'] = diff
    df = df[['CustomField_PublicationId', 'CustomField_PageNum', 'ReadTime_sec']]
    df.to_csv('results.csv', encoding='utf-8')

if __name__ == '__main__':
    main()
