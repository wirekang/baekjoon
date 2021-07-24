#!/bin/bash
dir=$(dirname $(realpath $0))
pDir=$dir/$PROBLEM

out="$(cat $pDir/in | node $pDir/js.js)"
rOut="$(cat $pDir/out)"

echo "Problem : $PROBLEM"
echo "Language: node.js"

if [[ "$out" == "$rOut" ]]; then
  echo "PASS"
else
  echo "FAIL"
  echo "----"
  echo "$out"
  echo "----"
  echo "$rOut"
fi