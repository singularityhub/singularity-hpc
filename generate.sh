#!/bin/bash

rm -rf _library/*
for module in $(shpc show); do          
    flatname=${module#/}
    name=$(echo ${flatname//\//-})
    echo "Generating docs for $module, _library/$name.md"
    shpc docgen $module > "_library/${name}.md"
done
