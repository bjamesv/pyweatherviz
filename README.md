# PyWeatherViz - US Future Weather Visualization

PyWeatherViz is a collection of Python modules to explore & visualize past weather data, with an aim toward understanding what future weather may be like.

PyWeatherViz is licensed under the GNU GPL v3

## Usage
 - 'api_info.py': Simple module, for the developer to save their NOAA National Centers for Environmental Information (NCEI) API key. For more information, see [notes](https://raw.githubusercontent.com/bjamesv/pyweatherviz/master/doc/ncei_api.md) and [NCEI API documentation](http://www.ncdc.noaa.gov/cdo-web/webservices/v2#gettingStarted).
 - 'visualize.py': Module to be run as a script. Outputs a Matplotlib visualization of 4 years of historic daily high & low temperatures (in degrees Celsius), overlaid with rainfall & snow depth (in CM), and vertical marks indicating weekday of interest (Saturdays).
  ```
python3 visualize.py
  ```
 - 'daily_json_to_dic.py': Module to retrieve Global Historical Climatology Network via NOAA NCIE, cache retrieved data to disk, and reformat the GHCN row-based output for improved handling.

## Output
PyWeatherViz started as an IPython Jupyter notebook, but has since been transitioned to set of plain, Python modules to generate & display a Matplotlib chart via pyplot.

![Montague, Michigan 2012-2015 weather for the period 17-MAR to 1-JUN of those years](https://raw.githubusercontent.com/bjamesv/pyweatherviz/master/doc/figure_1.png)

The darkest, orange line plot represents 2015 daily high temperatures over the target time period. Additional orange lines plots represent 2014-2012 daily high temps, with the oldest data being most faded/white.

The darkest, blue line plot represents 2015 daily low temperatures. With additional blue line plots representing 2012-2014 daily low temps (similarly fading to white as data goes further back in time).

Orange bar plots represent 2012-2015 daily rainfall in CM, with historical years progressively faded.

Blue bar plots represent 2012-2015 daily accumulated snow in CM. Increasingly historical years, increasingly faded.

Top-to-bottom, black, vertical bars represent Saturdays in 2016 over the visualized range of calendar days.

## Roadmap
 - [ ] Add legend detailing the meaning of each plot (data type, year, source weather station, etc.)
 - [ ] Replace hardcoded target date range to be visualized, weather station id, etc.
 - [ ] Clean up unused functions
 - [ ] Deprecate use of 15min precip CSV data (supplements 2013 data gaps, but slows script execution)
 - [ ] Improve visualization of missing data

Copyright (C) 2015 Brandon J. Van Vaerenbergh
