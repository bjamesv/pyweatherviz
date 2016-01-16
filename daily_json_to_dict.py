import api_info
from dateutil.parser import parse
import requests
import json
import pandas as pd
import logging

def get_ncei_daily_climate_dicts( date_start, date_xend):
    """
    obtain daily Global Historical Climatology Network data, via disk cache
    or NCEI web API registered developer token.
    """
    list_raw_dicts = _get_list_ncei_daily_climate( date_start, date_xend)
    # build dicts, & return the collection.
    return _get_daily_climate_dicts( list_raw_dicts)

def _get_list_ncei_daily_climate( date_start, date_xend):
    """
    returns collection of dicts, representing raw daily Global Historical
    Climatology Network data.
    """
    token = {'Token': api_info.key }
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?\
datasetid=GHCND&stationid=GHCND:USC00205567\
&startdate={start}&enddate={xend}\
&limit=1000"
    dict_range={
         'start': "{:%Y-%m-%d}".format( date_start)
        ,'xend' : "{:%Y-%m-%d}".format( date_xend)
        }
    file_cache = 'daily_json_{start}_{xend}.json'.format( **dict_range)
    try:
      cache = open( file_cache)
      logging.info('Opening local NCEI cache: ({})'.format(file_cache))
      list_json_response = json.load( cache)
    except FileNotFoundError:
      url_req = url.format( **dict_range)
      msg = 'Local NCIE cache ({}) not found, downloading: ({})'
      logging.info(msg.format(file_cache,url_req))
      # default requests behavior for connect timeout (infinte wait?) was no
      # good on a poorly configured IPv6 network (many, dead routes)
      max_s = (5,45) #docs.python-requests.org/en/latest/user/advanced/#timeouts
      list_json_response = requests.get( url_req, headers=token, timeout=max_s).json().get('results')
      json.dump( list_json_response, open( file_cache, 'w'))
    return list_json_response

def _get_daily_climate_dicts( list_daily_climate):
    """
    returns collection of dicts, each representing one day of daily Global
    Historical Climatolody Network data.

    >>> l = [{'date':'2013-01-01T00:00:00','datatype':'TMAX','value':25}\
            ,{'date':'2013-01-01T00:00:00','datatype':'SNWD','value':175}\
            ,{'date':'2013-01-01T00:00:00','datatype':'PRCP','value':90}]
    >>> out = _get_daily_climate_dicts( l)
    >>> from pprint import pprint
    >>> pprint( out)
    [{'DATE': datetime.datetime(2013, 1, 1, 0, 0),
      'PRCP_MM': 9.0,
      'SNWD_MM': 175,
      'TMAX_C': 2.5}]
    """
    list_one_row_per_day = []
    df_by_date = pd.DataFrame(list_daily_climate).groupby('date')
    for str_group in df_by_date.groups.keys():
        # build dict - add date
        dict_day = {'DATE': parse(str_group)}
        # extract TMAX
        df_day = df_by_date.get_group( str_group)
        if 'TMAX' in df_day.datatype.values:
            tmax_tenth_degC = df_day[ df_day.datatype == 'TMAX'].value
            dict_day['TMAX_C'] = int(tmax_tenth_degC) / 10
        # extract TMIN
        if 'TMIN' in df_day.datatype.values:
            tmin_tenth_degC = df_day[ df_day.datatype == 'TMIN'].value
            dict_day['TMIN_C'] = int(tmin_tenth_degC) / 10
        # extract snow depth in mm
        dict_day['SNWD_MM'] = 0
        if 'SNWD' in df_day.datatype.values:
            dict_day['SNWD_MM'] = int(df_day[ df_day.datatype == 'SNWD'].value)
        # extract precipitation in mm
        dict_day['PRCP_MM'] = 0
        if 'PRCP' in df_day.datatype.values:
            tenth_mm = int(df_day[ df_day.datatype == 'PRCP'].value)
            dict_day['PRCP_MM'] = tenth_mm / 10
        # add dict to list
        list_one_row_per_day.append( dict_day)
    return list_one_row_per_day
