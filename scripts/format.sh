#!/bin/bash
echo "Running black..."
black .
echo "Running flake8..."
flake8 --exclude=.git,__pycache__ .
echo "Done!"