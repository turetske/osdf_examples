## Example benchmarking


### Submission to OSpool

You must be on an AP node then,

`condor_submit benchmark.submit`

This will produce a out_*.json for each OSPool run. 

#### Aggregate resulting json files

`python aggregate_json.py`

#### Plot results

`python plot_aggregate.py`


