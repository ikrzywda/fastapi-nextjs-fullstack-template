#!/bin/bash

# Start the API server
cd app && PYTHONPATH=../ uvicorn main:app --reload 
