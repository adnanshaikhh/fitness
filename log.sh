#!/bin/bash

printf "Enter your weight ->"
read WEIGHT
echo "`date +%Y-%m-%dT%H:%M:%S%z`, $WEIGHT" >> weight.txt
