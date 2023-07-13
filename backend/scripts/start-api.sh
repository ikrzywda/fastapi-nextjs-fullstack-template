#!/bin/bash

# Start the API server
PYTHONPATH=app/ &&  cd app && uvicorn main:app --reload 
