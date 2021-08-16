#!/bin/sh 
ROOT=$(dirname $0)/../..
PYTHON=$ROOT/GoogleSheets/env/bin/python3 
MODULE=$ROOT/GoogleSheets/env/bin/uvicorn
# $PYTHON $MODULE -m GoogleSheets.main
$MODULE app:app --host 0.0.0.0 --port 8080

