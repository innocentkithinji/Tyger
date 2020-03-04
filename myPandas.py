# import pandas as pd
import  pandas_datareader as data
import datetime as dt

def read_data():
    """
    reads data of Tesla Stock from yahoo finanace and prints the 1st five columns and last 5 columns
    :return:
    """
    start_date = dt.datetime(2012, 1, 1)
    end_date = dt.datetime.now()

    df = data.DataReader('TSLA', 'yahoo', start_date, end_date)
    print(df.head())

    print(df.tail())


if __name__ == '__main__':
    read_data()