#!/bin/bash
dir=$(dirname $(realpath $0))
pDir=$dir/$PROB

out="$(cat $pDir/in | node $pDir/js.js)"
rOut="$(cat $pDir/out)"

echo "Problem : $PROB"
echo "Language: node.js"

echo "----expect"
echo "$rOut"
echo "----actual"
echo "$out"
echo "----"
