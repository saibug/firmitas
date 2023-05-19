#!/bin/sh

black --line-length=100 firmitas/
isort --profile=black firmitas/
flake8 --max-line-length=100 firmitas/