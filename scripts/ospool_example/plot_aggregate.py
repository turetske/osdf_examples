import matplotlib.pyplot as plt
import pdb
import geopy
import json

def calc_distance_from_NWSC(lat,lon):
    nwsc_lat = 41.127
    nwsc_lon = -104.894
    return geopy.distance.geodesic((nwsc_lat,nwsc_lon), (lat,lon)).km

def calculate_baseline_latency(dist):
    c = 299792 #km/s
    c_fiber = c * .67
    return dist/c_fiber # returns in units of seconds
    

benchmarks = json.load(open('aggregate.json')) 
pdb.set_trace()
for name,values in benchmarks.items():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"Direct downloads from {name}")
    ax.set_xticklabels(['HTTPS 20 MB','OSDF 20 MB - Cached', 'OSDF 20 MB - First Run'])
    ax.set_ylabel('Speed (MB/s)')
    ax.boxplot([values['20MB']['http'],values['20MB']['osdf'],values['20MB']['osdf_first']])
    ax.plot()
    fig.savefig(f'20{name}.png')
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"Direct downloads from {name}")
    ax.set_xticklabels(['HTTPS 200 MB','OSDF 200 MB - Cached', 'OSDF 200 MB - First Run'])
    ax.set_ylabel('Speed (MB/s)')
    ax.boxplot([http_benchmark_200,osdf_benchmark_200[1:],osdf_200_first])
    ax.plot()
    fig.savefig(f'200{name}.png')
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xticklabels(['HTTPS 500 MB','OSDF 500 MB - Cached','OSDF 500 MB - First Try'])
    ax.set_ylabel('Speed (MB/s)')
    ax.set_title(f"Direct downloads from {name}")
    ax.boxplot([http_benchmark_500,osdf_benchmark_500[1:],osdf_500_first])
    ax.plot()
    fig.savefig(f'500{name}.png')
    
