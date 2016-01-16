#%matplotlib inline
"""PyWeatherViz
'visualize.py' -- a python module to visualize the past weather, related to a
future range of dates.

Usage:
  visualize.py (-h | --help)
  visualize.py [<months>] [-v | --verbose]
  visualize.py [<start> <months>] [-v | --verbose]
  visualize.py [--start=<date> --months=<num>] [-v | --verbose]
  visualize.py [<start> <end>] [-v | --verbose]
  visualize.py [--start=<date> --end=<date>] [-v | --verbose]
  visualize.py

Options:
  -h --help     Show this screen.
  --start=<dt>  Starting date in the future, to retrieve weather history for.
                [default: tomorrow]
  --months=<n>  Number of months to visualize. [default: 3]
  --end=<date>  Visualization end date (End date will not be included in plot).
  -v --verbose  Explain what is being done. 

"""
from datetime import datetime
import math
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from docopt import docopt
import pandas as pd
import numpy as np
from datetime import timedelta
import operator
from pylab import plot, bar, show, xticks
import daily_json_to_dict
import logging

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
    forecast_start = datetime.now()+timedelta(days=1) #default: tomorrow
    forecast_xend = forecast_start+relativedelta(months=3)
    arguments = docopt(__doc__) #process command line arguments
    if arguments['--verbose']:
        logging.basicConfig(level=logging.DEBUG)
    if arguments['<start>'] is not None: #get start date
        forecast_start = parse(arguments['<start>'])
    if arguments['--start'] is not None:
        try:
            forecast_start = parse(arguments['--start']) #named opt overrides
        except TypeError:
            if arguments['--start'] != 'tomorrow': #no error, if default
                raise
    if arguments['--months'] is not None: #get range of dates/default
        num = int(arguments['--months'])
        forecast_xend = forecast_start+relativedelta(months=num)
    if arguments['<months>'] is not None:
        try:
            num = int(arguments['<months>'])
            forecast_xend = forecast_start+relativedelta(months=num)
        except ValueError:
            try:
                forecast_xend = parse(arguments['<months>'])
            except TypeError as e:
                msg = 'unable to tell if <end> or <month> specified. For help'\
                        +' see visualize.py -h'
                exception = Exception(msg)
                raise exception from e
    if arguments['<end>'] is not None: # specified end date overrides range
        forecast_xend = parse(arguments['<end>'])
    if arguments['--end'] is not None:
        forecast_xend = parse(arguments['--end'])
    #dictionary, describing range of dates for our forecast plot
    forecast_range = forecast_xend - forecast_start
    dict_plot = {'date_start': forecast_start
                ,'date_xend': forecast_xend
                }

    # add bar plots for SnowDepth in CM
    list_year_color_tuple = [ (4,'#ffffff') #white
                             ,(3,'#ddddff') #very faded blue
                             ,(2,'#bbbbff') #faded blue
                             ,(1,'#7777ff') #slightly faded blue
                            ]
    for snow_year_offset,str_color in list_year_color_tuple:
        #adjust to retrieve 4 years data,if forecast is 2+year in future
        delta_forecast_years_from_current = forecast_xend - datetime.now()
        days = delta_forecast_years_from_current.days
        forecast_xend_offset_years = math.floor( days/365.25)
        snow_year_offset += forecast_xend_offset_years
        dict_args = {'date_start': forecast_start-relativedelta(years=snow_year_offset)
                    ,'date_xend' : forecast_xend-relativedelta(years=snow_year_offset)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'SNWD_MM'
        dict_args['scale'] = 0.1 # scale MM of depth values, to CM depth
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_bars( **dict_args)

    # add bar plots for Precipitation in CM
    list_year_color_tuple = [ (6,'#ffee11') #very faded orange
                             ,(5,'#ffee33') #very faded orange
                             ,(4,'#ffee55') #very faded orange
                             ,(3,'#ffee77') #faded orange
                             ,(2,'#ffeebb') #slighty faded orange
                             ,(1,'#ffeeff') #orange
                            ]
    for rain_year_hist_offset,str_color in list_year_color_tuple:
        #adjust to retrieve 4 years data,if forecast is 2+year in future
        delta_forecast_years_from_current = forecast_xend - datetime.now()
        days = delta_forecast_years_from_current.days
        forecast_xend_offset_years = math.floor( days/365.25)
        rain_year_hist_offset += forecast_xend_offset_years
        dict_args = {'date_start': forecast_start-relativedelta(years=rain_year_hist_offset)
                    ,'date_xend' : forecast_xend-relativedelta(years=rain_year_hist_offset)
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
    list_year_color_tuple = [ (6,"#eeeeff") #very faded blue
                             ,(5,"#ddddff") #very faded blue
                             ,(4,"#ccccff") #very faded blue
                             ,(3,"#9999ff") #faded blue
                             ,(2,"#5555ff") #only slightly faded
                             ,(1,"#0000ff") #pure blue
                            ]
    for tmin_year_offset,str_color in list_year_color_tuple:
        #adjust to retrieve 4 years data,if forecast is 2+year in future
        delta_forecast_years_from_current = forecast_xend - datetime.now()
        days = delta_forecast_years_from_current.days
        forecast_xend_offset_years = math.floor( days/365.25)
        tmin_year_offset += forecast_xend_offset_years
        dict_args = {'date_start': forecast_start-relativedelta(years=tmin_year_offset)
                    ,'date_xend' : forecast_xend-relativedelta(years=tmin_year_offset)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'TMIN_C'
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_line( **dict_args)
    # add line plots for TMAX
    list_year_color_tuple = [ (4,"#ffcccc") #very faded red
                             ,(3,"#ff9999") #faded red
                             ,(2,"#ff5555") #only slightly faded
                             ,(1,"#ff0000") #pure red
                            ]
    for tmax_year_offset,str_color in list_year_color_tuple:
        #adjust to retrieve 4 years data,if forecast is 2+year in future
        delta_forecast_years_from_current = forecast_xend - datetime.now()
        days = delta_forecast_years_from_current.days
        forecast_xend_offset_years = math.floor( days/365.25)
        tmax_year_offset += forecast_xend_offset_years
        dict_args = {'date_start': forecast_start-relativedelta(years=tmax_year_offset)
                    ,'date_xend' : forecast_xend-relativedelta(years=tmax_year_offset)
                    ,'color'     : str_color
                    }
        dict_args['str_datatype'] = 'TMAX_C'
        dict_args['dict_plot'] = dict_plot
        add_daily_climate_line( **dict_args)

    xticks( rotation=25)
    show()
