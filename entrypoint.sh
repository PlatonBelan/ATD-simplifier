#!/bin/bash

if [[ $1 == 'simplify' ]]; then
    exec python3 console.py $2 $3
else
    exec $@
fi
