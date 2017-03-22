#!/usr/bin/env bash

set -e
script_dir=`dirname $0`
echo "Directory of script $0 is $script_dir"

python3 $script_dir/../getting-started/linear-regression-tf-core-version.py
python3 $script_dir/../getting-started/linear-regression-tf-contrib-version.py

python3 $script_dir/../mnist-for-ml-beginners/mnist-softmax.py
