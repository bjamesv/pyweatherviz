import api_info
from dateutil.parser import parse
import requests
import json
import pandas as pd

#obtain daily Global Historical Climatology Network data
token = {'Token': api_info.key }
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?\
datasetid=GHCND&stationid=GHCND:USC00205567\
&startdate=2015-03-17&enddate=2015-06-02\
&limit=1000"
file_cache = 'daily_json_mamj.json'
try:
  cache = open( file_cache)
  list_json_response = json.load( cache)
except FileNotFoundError:
  list_json_response = requests.get( url, headers=token).json().get('results')
  json.dump( list_json_response, open( file_cache, 'w'))

def get_daily_climate_list( list_daily_climate):
    """

    >>> l = [{'date':'2013-01-01T00:00:00','datatype':'TMAX','value':25}\
            ,{'date':'2013-01-01T00:00:00','datatype':'SNWD','value':175}]
    >>> out = get_daily_climate_list( l)
    >>> from pprint import pprint
    >>> pprint( out)
    [{'DATE': datetime.datetime(2013, 1, 1, 0, 0), 'SNWD_MM': 175, 'TMAX_C': 2.5}]
    """
    list_one_row_per_day = []
    df_by_date = pd.DataFrame(list_daily_climate).groupby('date')
    for str_group in df_by_date.groups.keys():
        # build dict - add date
        dict_day = {'DATE': parse(str_group) }
        # extract TMAX 
        df_day = df_by_date.get_group( str_group)
        tmax_tenth_degC = df_day[ df_day.datatype == 'TMAX'].value
        dict_day['TMAX_C'] = int(tmax_tenth_degC) / 10
        # extract snow depth in mm
        dict_day['SNWD_MM'] = 0
        if 'SNWD' in df_day.datatype.values:
            dict_day['SNWD_MM'] = int(df_day[ df_day.datatype == 'SNWD'].value)
        # add dict to list
        list_one_row_per_day.append( dict_day)
    return list_one_row_per_day