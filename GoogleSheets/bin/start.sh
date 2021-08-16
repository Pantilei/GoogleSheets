#!/bin/sh 
ROOT=$(dirname $0)/../..
PYTHON=$ROOT/GoogleSheets/env/bin/python3 
MODULE=$ROOT 
$PYTHON $MODULE -m GoogleSheets.main
