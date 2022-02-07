#!/bin/bash
dir=$(dirname $(realpath $0))
pDir=$dir/$PROB

out="$(cat $pDir/in | python $pDir/python.py)"
rOut="$(cat $pDir/out)"

echo "Problem : $PROB"
echo "Language: Python"

echo "----expect"
echo "$rOut"
echo "----actual"
echo "$out"
echo "----"
