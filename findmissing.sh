#!/bin/sh
names=$(cat ../../nomad-meta-info/meta_info/nomad_meta_info/crystal.nomadmetainfo.json | grep '"name":' | cut -f2 -d':' | cut -f2 -d'"' | sort -u)
cnt=$(for file in $* ; do echo $file ; done|wc -l)
python asjson.py $* > parsed.json
cnt2=$(cat parsed.json|grep '"parserStatus": "ParseSuccess"'|wc -l)
usednames=$(cat parsed.json|grep '"metaName":' | cut -f2 -d':' | cut -f2 -d'"' | sort -u)
unusednames=$(for name in $names; do echo $name ; done|grep2 -v $usednames $(for i in $(seq 1 20); do echo _value$i ; done))
echo "NAMES=" $names
echo "USEDNAMES=" $usednames
echo "UNUSEDNAMES="
for name in $unusednames; do echo $name ; done
echo "$cnt2 / $cnt"



