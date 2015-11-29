#%matplotlib inline
import csv
from datetime import datetime
str_zip49437_15min_precip = """STATION,STATION_NAME,DATE,QGAG,QPCP
COOP:205567,MONTAGUE 4 NW MI US,20130201 00:00,193,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130201 00:15,0,0
COOP:205567,MONTAGUE 4 NW MI US,20130201 01:15,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130202 10:00,194,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130205 00:00,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130205 20:30,195,10
COOP:205567,MONTAGUE 4 NW MI US,20130207 16:00,196,10
COOP:205567,MONTAGUE 4 NW MI US,20130207 18:00,197,10
COOP:205567,MONTAGUE 4 NW MI US,20130207 19:15,198,10
COOP:205567,MONTAGUE 4 NW MI US,20130207 21:15,199,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 00:15,200,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 13:00,201,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 14:00,199,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130208 14:15,200,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 14:30,201,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 15:45,199,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130208 16:00,200,10
COOP:205567,MONTAGUE 4 NW MI US,20130208 16:30,201,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 00:00,197,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130209 00:15,198,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 01:30,199,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 03:15,200,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 07:45,201,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 16:15,198,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130209 16:30,199,10
COOP:205567,MONTAGUE 4 NW MI US,20130209 16:45,200,10
COOP:205567,MONTAGUE 4 NW MI US,20130210 16:00,201,10
COOP:205567,MONTAGUE 4 NW MI US,20130210 18:15,202,10
COOP:205567,MONTAGUE 4 NW MI US,20130210 20:45,203,10
COOP:205567,MONTAGUE 4 NW MI US,20130211 00:00,204,10
COOP:205567,MONTAGUE 4 NW MI US,20130211 00:15,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130212 00:00,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130214 17:00,205,10
COOP:205567,MONTAGUE 4 NW MI US,20130214 21:15,206,10
COOP:205567,MONTAGUE 4 NW MI US,20130216 15:00,207,10
COOP:205567,MONTAGUE 4 NW MI US,20130216 19:15,208,10
COOP:205567,MONTAGUE 4 NW MI US,20130218 20:45,209,10
COOP:205567,MONTAGUE 4 NW MI US,20130218 21:45,210,10
COOP:205567,MONTAGUE 4 NW MI US,20130218 22:45,211,10
COOP:205567,MONTAGUE 4 NW MI US,20130219 00:00,212,10
COOP:205567,MONTAGUE 4 NW MI US,20130219 01:45,213,10
COOP:205567,MONTAGUE 4 NW MI US,20130219 15:00,8,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130219 15:15,29,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130219 16:00,30,10
COOP:205567,MONTAGUE 4 NW MI US,20130222 06:45,31,10
COOP:205567,MONTAGUE 4 NW MI US,20130223 18:30,32,10
COOP:205567,MONTAGUE 4 NW MI US,20130226 21:00,33,10
COOP:205567,MONTAGUE 4 NW MI US,20130227 03:00,34,10
COOP:205567,MONTAGUE 4 NW MI US,20130227 07:30,35,10
COOP:205567,MONTAGUE 4 NW MI US,20130227 10:30,36,10
COOP:205567,MONTAGUE 4 NW MI US,20130227 13:45,37,10
COOP:205567,MONTAGUE 4 NW MI US,20130228 23:45,37,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130301 00:00,37,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130301 00:15,37,0
COOP:205567,MONTAGUE 4 NW MI US,20130310 06:30,38,10
COOP:205567,MONTAGUE 4 NW MI US,20130310 09:45,39,10
COOP:205567,MONTAGUE 4 NW MI US,20130310 11:45,40,10
COOP:205567,MONTAGUE 4 NW MI US,20130310 16:30,41,10
COOP:205567,MONTAGUE 4 NW MI US,20130310 19:00,42,10
COOP:205567,MONTAGUE 4 NW MI US,20130310 20:30,43,10
COOP:205567,MONTAGUE 4 NW MI US,20130311 12:45,44,10
COOP:205567,MONTAGUE 4 NW MI US,20130312 23:00,45,10
COOP:205567,MONTAGUE 4 NW MI US,20130316 00:00,46,10
COOP:205567,MONTAGUE 4 NW MI US,20130318 12:30,47,10
COOP:205567,MONTAGUE 4 NW MI US,20130318 18:15,48,10
COOP:205567,MONTAGUE 4 NW MI US,20130321 04:30,49,10
COOP:205567,MONTAGUE 4 NW MI US,20130331 02:30,50,10
COOP:205567,MONTAGUE 4 NW MI US,20130401 00:00,50,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130401 00:15,50,0
COOP:205567,MONTAGUE 4 NW MI US,20130407 00:45,51,10
COOP:205567,MONTAGUE 4 NW MI US,20130408 10:45,52,10
COOP:205567,MONTAGUE 4 NW MI US,20130408 11:15,53,10
COOP:205567,MONTAGUE 4 NW MI US,20130408 12:00,54,10
COOP:205567,MONTAGUE 4 NW MI US,20130408 13:30,55,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 10:30,56,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 11:00,57,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 11:30,58,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 12:15,59,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 13:15,60,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 14:00,62,20
COOP:205567,MONTAGUE 4 NW MI US,20130409 14:15,63,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 14:45,64,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 15:15,65,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 15:30,66,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 16:00,67,10
COOP:205567,MONTAGUE 4 NW MI US,20130409 16:30,68,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 04:45,69,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 05:45,70,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 06:30,71,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 08:15,72,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 09:30,73,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 10:15,74,10
COOP:205567,MONTAGUE 4 NW MI US,20130410 19:15,75,10
COOP:205567,MONTAGUE 4 NW MI US,20130411 03:15,76,10
COOP:205567,MONTAGUE 4 NW MI US,20130411 04:00,77,10
COOP:205567,MONTAGUE 4 NW MI US,20130411 04:45,78,10
COOP:205567,MONTAGUE 4 NW MI US,20130411 16:30,79,10
COOP:205567,MONTAGUE 4 NW MI US,20130411 20:30,80,10
COOP:205567,MONTAGUE 4 NW MI US,20130412 01:15,81,10
COOP:205567,MONTAGUE 4 NW MI US,20130414 13:30,82,10
COOP:205567,MONTAGUE 4 NW MI US,20130415 21:00,83,10
COOP:205567,MONTAGUE 4 NW MI US,20130415 21:30,84,10
COOP:205567,MONTAGUE 4 NW MI US,20130415 22:30,85,10
COOP:205567,MONTAGUE 4 NW MI US,20130415 23:15,86,10
COOP:205567,MONTAGUE 4 NW MI US,20130416 00:00,87,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 15:00,88,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 16:15,89,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 16:45,90,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 17:15,91,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 17:30,92,10
COOP:205567,MONTAGUE 4 NW MI US,20130417 18:00,93,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 02:15,94,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 02:45,95,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 03:15,96,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 04:00,97,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 05:30,98,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 06:00,99,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 06:45,100,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 07:30,101,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 10:00,102,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 10:30,103,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 11:15,104,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 12:00,105,10
COOP:205567,MONTAGUE 4 NW MI US,20130418 23:45,106,10
COOP:205567,MONTAGUE 4 NW MI US,20130423 14:30,107,10
COOP:205567,MONTAGUE 4 NW MI US,20130423 15:15,108,10
COOP:205567,MONTAGUE 4 NW MI US,20130423 16:30,109,10
COOP:205567,MONTAGUE 4 NW MI US,20130423 18:15,110,10
COOP:205567,MONTAGUE 4 NW MI US,20130423 21:00,111,10
COOP:205567,MONTAGUE 4 NW MI US,20130424 00:15,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130426 00:00,-9999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130429 22:00,112,10
COOP:205567,MONTAGUE 4 NW MI US,20130430 05:15,113,10
COOP:205567,MONTAGUE 4 NW MI US,20130501 00:00,113,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130501 00:15,113,0
COOP:205567,MONTAGUE 4 NW MI US,20130503 17:00,114,10
COOP:205567,MONTAGUE 4 NW MI US,20130504 07:45,99999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130504 11:45,99999,99999
COOP:205567,MONTAGUE 4 NW MI US,20130504 12:00,114,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130510 00:30,115,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 03:15,116,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 06:00,117,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 08:30,118,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 09:00,119,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 09:30,120,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 10:00,121,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 11:00,122,10
COOP:205567,MONTAGUE 4 NW MI US,20130510 12:45,123,10
COOP:205567,MONTAGUE 4 NW MI US,20130511 13:15,124,10
COOP:205567,MONTAGUE 4 NW MI US,20130511 20:00,125,10
COOP:205567,MONTAGUE 4 NW MI US,20130521 02:15,126,10
COOP:205567,MONTAGUE 4 NW MI US,20130521 02:30,127,10
COOP:205567,MONTAGUE 4 NW MI US,20130521 03:00,128,10
COOP:205567,MONTAGUE 4 NW MI US,20130521 03:30,129,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 04:45,130,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 05:15,131,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 10:00,132,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 10:30,133,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 10:45,134,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 11:00,136,20
COOP:205567,MONTAGUE 4 NW MI US,20130522 11:15,137,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 11:30,140,30
COOP:205567,MONTAGUE 4 NW MI US,20130522 12:00,141,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 12:15,142,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 12:30,143,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 12:45,146,30
COOP:205567,MONTAGUE 4 NW MI US,20130522 13:30,147,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 13:45,148,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 16:30,149,10
COOP:205567,MONTAGUE 4 NW MI US,20130522 17:15,150,10
COOP:205567,MONTAGUE 4 NW MI US,20130523 06:15,151,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 07:00,152,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 09:45,153,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 10:15,154,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 10:45,155,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 11:15,156,10
COOP:205567,MONTAGUE 4 NW MI US,20130528 13:30,157,10
COOP:205567,MONTAGUE 4 NW MI US,20130529 00:30,158,10
COOP:205567,MONTAGUE 4 NW MI US,20130601 00:00,158,-9999
COOP:205567,MONTAGUE 4 NW MI US,20130601 00:15,-9999,0"""

#per: ftp://ftp.ncdc.noaa.gov/pub/data/cdo/documentation/PRECIP_15_documentation.doc
"""
QPCP: The amount of precipitation recorded at the station for the 15 minute period ending at the time specified for DATE above given in tenths or hundredths of inches depending on the value given in the Units element (see definition for Units below). Prior to January 1996 QPCP was the only observational element in this data set. The values 9999 or 99999 means the data value is missing. The maximum number of characters for this field is 8. This element is selectable when using the Climate Data Online interface for creating data output file.

QGAG: The volume of precipitation (calculated by weight) accumulated in measuring bucket as recorded at the station for the 15 minute period ending at the time specified for DATE above given in tenths or hundredths of inches depending on the value given in the Units element (see definition for Units below). This observational element was added with the January 1996 data. QGAG indicates that quarter-hour Fischer-Porter gage values are used. The values 9999 or 99999 means the data value is missing. The maximum number of characters for this field is 8. This element is selectable when using the Climate Data Online interface for creating data output file.

"""

from dateutil.parser import parse

import pandas as pd
import numpy as np
from datetime import timedelta
import operator
from pylab import plot, bar, show, xticks
import daily_json_to_dict

def add_bars( list_x_index, list_bar_vals, outline=False, color=None, width=0.8):
    # function to add a set of bars to our pylab plot
    bar_color=color
    outline_color=None
    if outline: # set color for outline & make bar transparent
        outline_color=bar_color
        bar_color=None
    bar(list_x_index, list_bar_vals,edgecolor=outline_color,color=bar_color,width=width)

def add_lines( list_x_index, list_bar_vals, color='blue'):
    # function to add a line plot to our pylab plot
    dict_kwargs = {
         'linestyle':   'solid'
        ,'marker'   :   'o'
        ,'color'    :   color
        ,'markersize':  2
        }
    plot(list_x_index, list_bar_vals, **dict_kwargs)

# Render a set of black outlines for each Saturday in 2015
sat_height = 100
# Hight of the bars for Saturday
find_sat = lambda x: sat_height if x.weekday()==5 else 0
# function to identify Saturdays

def clean_15_min_precip( list_rain_dicts):
    list_output = []
    for row in list_rain_dicts:
        #parse date & rain
        row['DATE'] = parse(row['DATE'])
        row['QPCP'] = int(row['QPCP'])
        #remove bad data
        bad_qpcp = row['QPCP'] in( -9999,99999)
        if bad_qpcp:
            row['QPCP'] = 0 #replace missing w/ 0
        bad_qgag = row['QGAG'] in( -9999,99999)
        if bad_qgag:
            row['QGAG'] = 0 #replace missing w/ 0
        list_output.append( row)
    return list_output

def remove_dates_before( list_of_dicts, date):
    """

    >>> l=[{'DATE':parse('2011-1-1')},{'DATE':parse('2015-1-1')}]
    >>> remove_dates_before( l, parse('2015-1-1'))
    [{'DATE': datetime.datetime(2015, 1, 1, 0, 0)}]
    """
    list_return = list()
    for d in list_of_dicts:
        if d['DATE'] >= date:
            list_return.append( d)
    return list_return

def index_dates( list_of_rain_dict, date_start, date_xend, scale=1):
    """
    return a list of floats ranging from 0 to scale, distributed based on the
    'DATE' values in the referenced list of rain dictionaries.

    >>> index_dates( [{'DATE': parse('2015-nov-1 12:00pm')}], datetime(2015,11,1), datetime(2015,11,2))
    [0.5]
    >>> index_dates( [{'DATE': parse('2015-nov-1 12:00pm')}], datetime(2015,11,1), datetime(2015,11,2)\
        , scale=10)
    [5.0]
    >>> index_dates( [{'DATE': parse('2015-nov-1 12:00pm')}\
                     ,{'DATE': parse('2015-nov-1 6:00pm')}], datetime(2015,11,1), datetime(2015,11,2))
    [0.5, 0.75]
    """
    timedelta_distance = date_xend - date_start
    list_output = []
    for dict_rain in list_of_rain_dict:
        date = dict_rain['DATE']
        distance = (date - date_start) / timedelta_distance
        list_output.append( distance*scale)
    return list_output

def add_daily_climate_line( date_start, date_xend, dict_plot, str_datatype='TMAX_C', color='blue'):
    #adds a historic, daily climate line to our forecast plot
    list_climate_daily_unordered = daily_json_to_dict.get_ncei_daily_climate_dicts(date_start, date_xend)
    list_climate_daily_clean = [ x for x in list_climate_daily_unordered if str_datatype in x.keys() ]
    list_climate_daily = sorted(list_climate_daily_clean, key=operator.itemgetter('DATE'))
    # prepare y-values, x-index & add bars for the referenced daily climate value
    list_values = [ x[str_datatype] for x in list_climate_daily]
    # plot list_values along x-axis relative to the target, forecast-year
    forecast_plot_start_date = dict_plot['date_start']
    timedelta_to_forecast_start = forecast_plot_start_date - date_start
    list_dates = [ x['DATE']+timedelta_to_forecast_start for x in list_climate_daily]
    add_lines( list_dates, list_values, color)

def add_daily_climate_bars( date_start, date_xend, dict_plot, str_datatype='SNWD_MM', color='white', scale=1):
    #adds historic, daily climate bars to our forecast plot
    list_climate_daily_unordered = daily_json_to_dict.get_ncei_daily_climate_dicts(date_start, date_xend)
    list_climate_daily_clean = [ x for x in list_climate_daily_unordered if str_datatype in x.keys() ]
    list_climate_daily = sorted(list_climate_daily_clean, key=operator.itemgetter('DATE'))
    # prepare y-values, x-index & add bars for the referenced daily climate value
    list_values = [ x[str_datatype]*scale for x in list_climate_daily]
    # plot list_values along x-axis relative to the target, forecast-year
    forecast_plot_start_date = dict_plot['date_start']
    timedelta_to_forecast_start = forecast_plot_start_date - date_start
    list_dates = [ x['DATE']+timedelta_to_forecast_start for x in list_climate_daily]
    add_bars( list_dates, list_values, color=color)

if __name__ == "__main__":
    #dictionary, describing range of dates for our forecast plot
    str_year = '2017'
    str_start_mondd = '-mar-17'
    str_xend_mondd = '-june-2'
    dict_plot = {'date_start': parse(str_year+str_start_mondd)
                ,'date_xend': parse(str_year+str_xend_mondd)
                }

    # add bar plots for SnowDepth in CM
    list_year_color_tuple = [ ('2012','#ffffff') #white
                             ,('2013','#ddddff') #very faded blue
                             ,('2014','#bbbbff') #faded blue
                             ,('2015','#7777ff') #slightly faded blue
                            ]
    for str_year_snow,str_color in list_year_color_tuple:
        dict_args = {'date_start': parse(str_year_snow+str_start_mondd)
                    ,'date_xend' : parse(str_year_snow+str_xend_mondd)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'SNWD_MM'
        dict_args['scale'] = 0.1 # scale MM of depth values, to CM depth
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_bars( **dict_args)

    # add bar plots for Precipitation in CM
    list_year_color_tuple = [ ('2012','#ffeedd') #very faded orange
                             ,('2013','#ffeebb') #faded orange
                             ,('2014','#ffee77') #slighty faded orange
                             ,('2015','#ffeeff') #orange
                            ]
    for str_year_rain,str_color in list_year_color_tuple:
        dict_args = {'date_start': parse(str_year_rain+str_start_mondd)
                    ,'date_xend' : parse(str_year_rain+str_xend_mondd)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'PRCP_MM'
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_bars( **dict_args)

    # Add a black outline for each Saturday in 2017 from mid-March to June
    x_dates = pd.date_range(dict_plot['date_start'], dict_plot['date_xend'])
    saturdays = tuple(find_sat(date) for date in x_dates)
    add_bars( x_dates, saturdays, outline=True, color='black', width=0.2)

    # plot lines for daily climate Min. temp. values
    list_year_color_tuple = [ ('2012',"#ccccff") #very faded blue
                             ,('2013',"#9999ff") #faded blue
                             ,('2014',"#5555ff") #only slightly faded
                             ,('2015',"#0000ff") #pure blue
                            ]
    for str_year_tmin,str_color in list_year_color_tuple:
        dict_args = {'date_start': parse(str_year_tmin+str_start_mondd)
                    ,'date_xend' : parse(str_year_tmin+str_xend_mondd)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'TMIN_C'
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_line( **dict_args)
    # add line plots for TMAX
    list_year_color_tuple = [ ('2012',"#ffcccc") #very faded red
                             ,('2013',"#ff9999") #faded red
                             ,('2014',"#ff5555") #only slightly faded
                             ,('2015',"#ff0000") #pure red
                            ]
    for str_year_tmax,str_color in list_year_color_tuple:
        dict_args = {'date_start': parse(str_year_tmax+str_start_mondd)
                    ,'date_xend' : parse(str_year_tmax+str_xend_mondd)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'TMAX_C'
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_line( **dict_args)

    list_2013_rain_dict = csv.DictReader(str_zip49437_15min_precip.splitlines())
    date_start_2013 = parse('2013'+str_start_mondd)
    #2013 precipitation, 15min resolution
    clean_list_2013 =  remove_dates_before( clean_15_min_precip( list_2013_rain_dict), date_start_2013)

    timedelta_to_forecast_year = dict_plot['date_start'] - date_start_2013
    dates_2013 = [ x['DATE']+timedelta_to_forecast_year for x in clean_list_2013]
    inches_2013 = [ x['QPCP'] for x in clean_list_2013]
    add_bars( dates_2013, inches_2013, color='orange')
    xticks( rotation=25)
    show()