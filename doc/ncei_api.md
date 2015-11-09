# NCEI API
http://www.ncdc.noaa.gov/cdo-web/webservices/v2#gettingStarted

# Datasets
```bash
curl -H "Token: MYTOKEN1" http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets
```

Datasetid GHCND (GLOBAL HISTORICAL CLIMATOLOGY NETWORK; Daily) appears best.

JSON api output ought to be easier to use than:
 http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
 ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily

# Stations
FIPS code (XYABCD; XY-state, ABC-county)
http://www.nws.noaa.gov/nwr/coverage/ccov.php?State=MI

Muskegon: 26121

## Climate Data Stations
http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:26121&limit=1000

Montague 4 NW; locationid: USC00205567

```python
>>> for row in r.json().get('results'):
...   min = parse(row['mindate'])
...   mi = parse(row['mindate'])
...   ma = parse(row['maxdate'])
...   targ = parse('2013-mar-17')
...   if mi <= targ and ma >= targ:
...     print(row)
... 
{'longitude': -86.3029, 'elevation': 187.5, 'name': 'NORTON SHORES 3.0 WNW, MI US', 'maxdate': '2015-08-19', 'mindate': '2010-05-01', 'id': 'GHCND:US1MIMG0012', 'datacoverage': 0.5934, 'elevationUnit': 'METERS', 'latitude': 43.1844}
{'longitude': -86.2364, 'elevation': 189.3, 'name': 'MUSKEGON 3.5 SSE, MI US', 'maxdate': '2015-11-01', 'mindate': '2010-05-01', 'id': 'GHCND:US1MIMG0013', 'datacoverage': 0.7229, 'elevationUnit': 'METERS', 'latitude': 43.1791}
{'longitude': -86.4175, 'elevation': 198.1, 'name': 'MONTAGUE 4 NW, MI US', 'maxdate': '2015-09-30', 'mindate': '1893-02-01', 'id': 'GHCND:USC00205567', 'datacoverage': 1, 'elevationUnit': 'METERS', 'latitude': 43.4614}
{'longitude': -86.2037, 'elevation': 192.9, 'name': 'MUSKEGON 4 SE, MI US', 'maxdate': '2014-11-29', 'mindate': '2012-10-01', 'id': 'GHCND:USC00205713', 'datacoverage': 0.4233, 'elevationUnit': 'METERS', 'latitude': 43.1839}
{'longitude': -86.23667, 'elevation': 190.5, 'name': 'MUSKEGON CO AIRPORT, MI US', 'maxdate': '2015-11-04', 'mindate': '1896-06-01', 'id': 'GHCND:USW00014840', 'datacoverage': 1, 'elevationUnit': 'METERS', 'latitude': 43.17111}
```

# Query

http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00205567&startdate=2015-03-17&enddate=2015-06-02&limit=1000
