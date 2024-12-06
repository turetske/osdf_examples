import matplotlib.pyplot as plt
import pdb
import geopy.distance
import json
import math

def calc_distance_from_NWSC(lat,lon):
    nwsc_lat = 41.127
    nwsc_lon = -104.894
    return geopy.distance.geodesic((nwsc_lat,nwsc_lon), (lat,lon)).km

def calculate_baseline_latency(dist):
    c = 299792 #km/s
    c_fiber = c * .67
    return math.floor((dist/c_fiber)*2) # returns in units of seconds
    

benchmarks = json.load(open('aggregate.json')) 

for name,values in benchmarks.items():

    distance = 'unknown'
    baseline_latency = 'unknown'
    try:
        distance = calc_distance_from_NWSC(values['Site']['Latitude'], values['Site']['Longitude'])
        baseline_latency = calculate_baseline_latency(distance)
    except KeyError:
        pass # unknown location
    number_of_runs = len(values['20MB']['osdf'])
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"20MB Direct downloads from {name}. {distance} km from NWSC (n={number_of_runs})")
    ax.set_xticklabels(['HTTPS 20 MB','OSDF 20 MB - Cached', 'OSDF 20 MB - First Run'])
    ax.set_ylabel('Elapsed Time (s)')
    ax.boxplot([values['20MB']['http'],values['20MB']['osdf'],values['20MB']['osdf_first']])
    ax.plot()
    fig.savefig(f'20{name}.png')
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"200MB Direct downloads from {name}. {distance} km from NWSC (n={number_of_runs})")
    ax.set_xticklabels(['HTTPS 200 MB','OSDF 200 MB - Cached', 'OSDF 200 MB - First Run'])
    ax.set_ylabel('Elapsed Time (s)')
    ax.boxplot([values['200MB']['http'],values['200MB']['osdf'],values['200MB']['osdf_first']])
    ax.plot()
    fig.savefig(f'200{name}.png')
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xticklabels(['HTTPS 500 MB','OSDF 500 MB - Cached','OSDF 500 MB - First Try'])
    ax.set_ylabel('Elapsed Time (s)')
    ax.set_title(f"500MB Direct downloads from {name}. {distance} km from NWSC (n={number_of_runs})")
    ax.boxplot([values['500MB']['http'],values['500MB']['osdf'],values['500MB']['osdf_first']])
    ax.plot()
    fig.savefig(f'500{name}.png')
    
