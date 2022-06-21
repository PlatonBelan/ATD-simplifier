#!/bin/bash

if [[ $1 == 'simplify' ]]; then
    exec python3 simplifier.py $2 $3
else 
    exec $@
fi
