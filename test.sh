#!/bin/bash

find . -name "*.pyc" -exec rm -f {} \;
rm -rf __pycache__

python -m unittest discover

