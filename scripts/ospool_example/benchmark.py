# Display output of plots directly in Notebook
import sys
import os
import matplotlib.pyplot as plt
import fsspec
import fsspec.implementations.http as fshttp
from pelicanfs.core import PelicanFileSystem, PelicanMap, OSDFFileSystem
import time
import gc
import socket
hostname = socket.gethostname()
import json
import random


def convert_to_speed(times,size):
    """Convert elapsed time to speed. Output units are in given size/time"""
    return [size/x for x in times]

def read_https(url, repeat=10):
    """Given url, read into memory, return elapsed time"""
    results = []
    print(url)
    for i in range(repeat):
        start = time.time()
        fh = fsspec.open(url)
        test = fh.open().read()
        end = time.time()
        results.append(end-start)

    return results



if len(sys.argv) > 1:
    hostname = sys.argv[1]

# Organization of results
results = {hostname:{
    "20MB":{},
    "200MB":{},
    "500MB":{}}
    }
https_url = 'https://data.rda.ucar.edu/d083002/grib2/2016/2016.01/fnl_20160101_00_00.grib2' # ~ 17 MB
https_url_200 = 'https://data.rda.ucar.edu/d131003/anl/anl_mean_1836_CAPE_sfc.nc' # ~ 200 MB
https_url_500 = 'https://data.rda.ucar.edu/d084001/2024/20241109/gfs.0p25.2024110900.f000.grib2' # ~ 500 MB
osdf_url = https_url.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')
osdf_url_200 = https_url_200.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')
osdf_url_500 = https_url_500.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')


print('** http tests')
http_benchmark_20  = read_https(https_url)
http_benchmark_200 = read_https(https_url_200)
http_benchmark_500 = read_https(https_url_500)

print('** osdf tests')
osdf_benchmark_20  = read_https(osdf_url)
osdf_benchmark_200 = read_https(osdf_url_200)
osdf_benchmark_500 = read_https(osdf_url_500)

print('** osdf first pull tests')
reps = 11
osdf_500_first = []
### Attempt to randomize
osdf_url_500 = osdf_url_500.replace('2024', str(random.randint(2016,2023)))
osdf_url_500 = osdf_url_500.replace('11', str(random.randint(10,12)))
osdf_url_500 = osdf_url_500.replace('09', str(random.randint(12,28)))
for i in range(random.randint(1,15),reps):
    new_url = osdf_url_500.replace('f000','f'+f'{i*3}'.zfill(3))
    print(new_url)
    start = time.time()
    try:
        osdf_file = fsspec.open(new_url)
        test = osdf_file.open().read()
        end = time.time()
        osdf_500_first.append(end-start)
        print(end-start)
    except:
        print(f'failed run {i}')
    gc.collect()

reps = 11
osdf_200_first = []
rand_year = random.randint(1836,1980)
for i in range(rand_year,rand_year+reps):
    new_url = osdf_url_200.replace('1837', f'{i}')
    print(new_url)
    start = time.time()
    try:
        osdf_file = fsspec.open(new_url)
        test = osdf_file.open().read()
        end = time.time()
        osdf_200_first.append(end-start)
        print(end-start)
    except:
        print(f'failed run {i}')


reps = 11
osdf_20_first = []
for i in range(2,reps):
    new_url = osdf_url.replace('20160101','201601'+f'{i}'.zfill(2))
    month = str(random.randint(1,12)).zfill(2)
    new_url = new_url.replace('201601','2016'+month)
    new_url = new_url.replace('2016.01','2016.'+month)
    new_url = new_url.replace('2016',str(random.randint(2016,2023)))
    print(new_url)
    start = time.time()
    try:
        osdf_file = fsspec.open(new_url)
        test = osdf_file.open().read()
        end = time.time()
        osdf_20_first.append(end-start)
    except:
        print(f'failed run {i}')

results[hostname]['20MB']['http'] = http_benchmark_20
results[hostname]['20MB']['osdf'] = osdf_benchmark_20[1:]
results[hostname]['20MB']['osdf_first'] = osdf_20_first

results[hostname]['200MB']['http'] = http_benchmark_200
results[hostname]['200MB']['osdf'] = osdf_benchmark_200[1:]
results[hostname]['200MB']['osdf_first'] = osdf_200_first

results[hostname]['500MB']['http'] = http_benchmark_500
results[hostname]['500MB']['osdf'] = osdf_benchmark_500[1:]
results[hostname]['500MB']['osdf_first'] = osdf_500_first

fnum = random.randint(1,1000000)
out_filename = f'out_{fnum}.json'
json.dump(results, open(out_filename,'w'))

