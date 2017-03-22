#!/usr/bin/env bash

set -e

(
cd ../getting-started/
python3 linear-regression-tf-core-version.py
python3 linear-regression-tf-contrib-version.py

cd ../mnist-for-ml-beginners/
python3 mnist-softmax.py
)
