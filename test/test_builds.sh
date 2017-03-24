#!/usr/bin/env bash

set -e
script_dir=`dirname $0`
echo "Directory of script $0 is $script_dir"

python3 $script_dir/../getting-started/linear-regression-tf-core-version.py
# the following script is disabled: the code (copied from TensorFlow tutorial) produces segfaults
# python3 $script_dir/../getting-started/linear-regression-contrib-version.py
# python3 $script_dir/../getting-started/linear-regression-custom.py

( cd $script_dir/../mnist/ && python3 mnist-softmax.py )
