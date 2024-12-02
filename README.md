# OSDF_Examples

## About
Contains Jupyter notebook workflows which access climate data from various [OSDF](https://osg-htc.org/services/osdf.html) origins using [PelicanFS](https://github.com/PelicanPlatform/pelicanfs). The examples include workflows where computations are executed on various platforms like NCAR's Casper, TACC's Stampede3 and cloud computing platforms like Jetstream2. 


## Example Workflows
1) Access CESM2 LENS data from the AWS opendata origin and the NCAR data origin and
   - a) [Benchmark](notebooks/ndc_workflows/aws_benchmark.ipynb) data access speeds for subsets of various sizes.
   - b) [Bias-correct](notebooks/cesm_bias.ipynb) surface temperature using ERA5 reanalysis. 
   - c) [Compute](notebooks/cesm_oceanheat.ipynb) surface ocean heat content. 
2) Access NOAA SONAR data from the AWS origin to [plot echograms](notebooks/ndc_workflows/sonar_ai.ipynb)
3) Benchmark data access speeds from the NCAR data [origin](notebooks/ndc_workflows/ncar_benchmark.ipynb) using the DART reanalysis dataset
4) Benchmark data access speeds from the NCAR's data [origin](notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb), when the data is accessed from the OSPool's access point AP40
5) Run temperature bias-correction workflow on
   - a) [Stampede3](notebooks/cesm_osdf_stampede3.ipynb)
   - b) [NCAR's Casper](notebooks/cesm_posix_bias.ipynb)
6) [Compute](notebooks/geocat_climatology.ipynb) climatological average of daily temperature data using the [geocat-comp](https://geocat-comp.readthedocs.io/en/stable/examples/climatology_average.html) package
 

