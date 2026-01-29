---
title: Introduction
author:  Harsha R. Hampapura
date: 2026-1-28
---

# Introduction

Welcome to the **OSDF Examples** repository! This repository provides example notebooks and scripts that demonstrate how to access data from via the Open Science Data Federation([OSDF](https://osg-htc.org/services/osdf.html)) using the using [PelicanFS](https://github.com/PelicanPlatform/pelicanfs) software. All the notebooks demonstrate how to stream geoscience data into your workflows and perform an interesting calculation/visualization. If you wish to learn more about OSDF and/or Pelican, please refer to the [OSDF cookbook](https://projectpythia.org/osdf-cookbook/).

:::{warning} Important Notice
This jupyter book is under active development. You will need to set up your python enviroment using the requirements.txt file before running any of the notebooks. Please open an issue on the associated github repository to report any bugs or suggest improvements.
::: 

## How is the repository organized?

This repository is organized by into various sections (mostly) based on the data origins from which the data is accessed and the computational platforms used to execute the notebooks.

- **NCAR GDEX workflows** (Workflows that are executed on NCAR's HPC system Casper)
    - NCAR Data Origin (Illustrate data streaming from NCAR's OSDF origin)
    - Other Data Origins (Illustrate data streaming from other OSDF origins like AWS etc)
    - ML Workflows (Machine Learning Workflows)
- **Other Computational Platforms** (Workflows that are executed other HPC, cloud computing platforms)
- **NDC Workflows** (Workflows that were developed as a part of the National Discovery Cloud (NDC) initiative )
- **Scripts** (Python scripts and any content that is not a jupyter notebook)

### 🌐 Access Methods
Some of these notebooks use intake/intake-ESM catalogs in conjunction with the PelicanFS software to stream data. Others directly use the PelicanFS software to load data into xarray.

## Repository Structure
- **`docs/`** - Introductory markdown files for each section
- **`notebooks/`** - All computational workflows/examples archived as jupyter notebooks
- **`scripts/`** - Python scripts and any content that is not a jupyter notebook