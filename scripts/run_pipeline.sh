#!/bin/bash
echo "Running pipelines ..."
docker-compose up -d  
sleep 3
PYTHONPATH=. python week3/sales_pipeline.py