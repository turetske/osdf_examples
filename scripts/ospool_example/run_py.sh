#!/bin/bash
tar -xzf my_env.tar.gz
export PYTHONPATH=$PWD/my_env
cat .machine.ad
exit 0
python3 benchmark.py `grep '^GLIDEIN_Site ' .machine.ad | awk '{print $3}'`
