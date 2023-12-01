#!/bin/bash

if [ "$2" == "prod" ]; then
    cat "$1.input" | "./$1.py"
else
    cat "$1.test" | "./$1.py"
fi