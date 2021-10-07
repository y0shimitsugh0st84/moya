#!/bin/bash
IFS=$'\n'
for i in `cat us`
do
   echo "'$i'," >> SHIT
done
