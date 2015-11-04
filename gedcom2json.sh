#!/bin/bash

if [[ -z "$1" ]] || [[ -z "$2" ]]; then
    echo "Usage: $(basename $0) path/to/gedcom.ged path/to/entailed_output.json"
    exit 1
fi

ONTONAME=$(basename $1)
TMPDIR=$(dirname $2)/$ONTONAME.$$

if [ ! -d "$TMPDIR" ]; then
    mkdir -p $TMPDIR
fi

cp data/header.ttl $TMPDIR/$ONTONAME.ttl
./gedcom2ttl.py $1 >> $TMPDIR/$ONTONAME.ttl
./infer.py $TMPDIR/$ONTONAME.ttl
./ttl2json.py $TMPDIR/$ONTONAME.ttl.inferred > $2

echo "$2 is ready, used ontologies are in $TMPDIR"
exit 0
