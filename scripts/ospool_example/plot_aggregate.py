import matplotlib.pyplot as plt
import pdb
import geopy.distance
import json
import math
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os,sys

def calc_distance_from_NWSC(lat,lon):
    nwsc_lat = 41.127
    nwsc_lon = -104.894
    return math.floor(geopy.distance.geodesic((nwsc_lat,nwsc_lon), (lat,lon)).km)

def calculate_baseline_latency(dist):
    c = 299792 #km/s
    c_fiber = c * .67
    return round((dist/c_fiber)*2*1000,3) # returns in units of seconds
    

benchmarks = json.load(open('aggregate.json')) 

# Make one figure for each benchmark entry
for name,values in benchmarks.items():
    distance = 'unknown'
    baseline_latency = 'unknown'
    try:
        distance = calc_distance_from_NWSC(values['Site']['Latitude'], values['Site']['Longitude'])
        baseline_latency = calculate_baseline_latency(distance)
    except KeyError:
        pass # unknown location
    number_of_runs = len(values['20MB']['osdf'])

    fig = plt.figure(figsize=(20, 12))
    axs = fig.subplots(2, 2)

    axs[0,0].set_title(f"20MB Direct downloads from {name}. {distance} km from NWSC\nn={number_of_runs}  Minimum latency: {baseline_latency} ms")
    axs[0,0].set_xticklabels(['HTTPS 20 MB','OSDF 20 MB - Cached', 'OSDF 20 MB - First Run'])
    axs[0,0].set_ylabel('Elapsed Time (s)')
    axs[0,0].boxplot([values['20MB']['http'],values['20MB']['osdf'],values['20MB']['osdf_first']])
    
    axs[0,1].set_title(f"200MB Direct downloads from {name}. {distance} km from NWSC\nn={number_of_runs}  Minimum latency: {baseline_latency} ms")
    axs[0,1].set_xticklabels(['HTTPS 200 MB','OSDF 200 MB - Cached', 'OSDF 200 MB - First Run'])
    axs[0,1].set_ylabel('Elapsed Time (s)')
    axs[0,1].boxplot([values['200MB']['http'],values['200MB']['osdf'],values['200MB']['osdf_first']])
    
    axs[1,1].set_xticklabels(['HTTPS 500 MB','OSDF 500 MB - Cached','OSDF 500 MB - First Try'])
    axs[1,1].set_ylabel('Elapsed Time (s)')
    axs[1,1].set_title(f"500MB Direct downloads from {name}. {distance} km from NWSC\nn={number_of_runs}  Minimum latency: {baseline_latency} ms")
    axs[1,1].boxplot([values['500MB']['http'],values['500MB']['osdf'],values['500MB']['osdf_first']])

    conus_proj = ccrs.LambertConformal(central_longitude=-96,central_latitude=39.0)
    axs[1,0].remove()
    ax = fig.add_subplot(2, 2, 3, projection=conus_proj)
    ax.set_title(f"NWSC to {name}")
    ax.set_extent([-120,-70,22,50])
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.OCEAN, facecolor='#CCFEFF')
    ax.add_feature(cfeature.LAKES, facecolor='#CCFEFF')
    ax.add_feature(cfeature.RIVERS, facecolor='#CCFEFF')
    ax.add_feature(cfeature.LAND, facecolor='#FFE9B5')
    state_borders = cfeature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes', scale='50m', facecolor='#FFE9B5')
    ax.add_feature(state_borders, edgecolor='black') 
    nwsc_lat,nwsc_lon = (41.127, -104.894)
    try:
        ax.plot([nwsc_lon,float(values['Site']['Longitude'])],[nwsc_lat,values['Site']['Latitude']],linewidth=4, transform=ccrs.PlateCarree())
    except:
        ax.plot([nwsc_lon,-104],[nwsc_lat,41],linewidth=4, transform=ccrs.PlateCarree())

    fig.savefig(f'{name}.png')
