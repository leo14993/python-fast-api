#!/bin/bash

uvicorn main:app --reload --host $1 --port $2
