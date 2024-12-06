import json
import glob
import pdb
import geopy



def swap_resource_name(name):
    """change the resource name of a few special cases"""
    if name == 'Colorado':
        return 'UColorado_HEP'
    if name == 'Lehig':
        return 'Lehigh - Hawk'
    if 'gpgrid' in name.lower():
        return 'GPGRID'
    if name == 'Wisconsin':
        return 'CHTC'
    if name == 'Pervasiv':
        return 'Jetstream2-IU'
    if name == 'UChicago':
        return 'GC1'
    if name == 'Ne':
        return 'CMS Glidein Systems'
    return name
files = glob.glob('out*.json')



rgs = json.load(open('resource_group_summary'))

results = {}
for _file in files:
    benchmarks = json.load(open(_file))
    resource_name = list(benchmarks.keys())[0]
    if resource_name not in results:
        try:
            location_info = rgs[swap_resource_name(resource_name)]['Site']
        except KeyError:
            print(f'{resource_name} not found')
            location_info = {}
        results[resource_name] = benchmarks[resource_name]
        results[resource_name]['Site'] = location_info
    else:
        for i,j in benchmarks[resource_name].items():
            if i == 'Site': 
                continue
            for k,l in j.items():
                results[resource_name][i][k].extend(l)



with open('aggregate.json', 'w') as fh:
    json.dump(results, fh)

print(results.keys())




