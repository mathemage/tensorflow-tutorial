#! /usr/bin/bash
files="t10k-images-idx3-ubyte.gz t10k-labels-idx1-ubyte.gz train-images-idx3-ubyte.gz train-labels-idx1-ubyte.gz"
url="https://web.archive.org/web/20150906081542/http://yann.lecun.com/exdb/mnist/"

for file in $files; do
  command="wget $url$file"
  $command
done
