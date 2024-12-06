#!/bin/bash
tar -xzf my_env.tar.gz
export PYTHONPATH=$PWD/my_env
python3 benchmark.py `grep '^GLIDEIN_Site ' .machine.ad | awk '{print $3}' | cut -c 2- | rev | cut -c 2- | rev`
