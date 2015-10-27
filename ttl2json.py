#!/usr/bin/env python

import os, sys
import json

import rdflib


RELS_TO_DRAW = ['isWifeOf', 'isMotherOf']
RELS_TO_INFER = ['hasFather', 'isFatherOf', 'hasGrandParent', 'isGrandParentOf', 'isGreatGrandParentOf', 'hasGreatGrandParent', 'isUncleOf', 'hasUncle', 'isGreatUncleOf', 'hasGreatUncle', 'isAuntOf', 'hasAunt', 'isGreatAuntOf', 'hasGreatAunt', 'isFirstCousinOf', 'isSecondCousinOf', 'isThirdCousinOf']
RELS_OF_INTEREST = RELS_TO_DRAW + RELS_TO_INFER

try: workpath = sys.argv[1]
except IndexError: sys.exit("No path defined!")

g = rdflib.Graph()
g.parse(workpath, format="turtle")

triples = []

FHKB = rdflib.Namespace("http://www.example.com/genealogy.owl#")

def dump(uriref):
    return uriref.split('#')[-1]

for i in g.subjects(object=FHKB.Person):
    for p, o in g.predicate_objects(subject=i):
        if p.startswith(FHKB) and dump(p) in RELS_OF_INTEREST:
            triples.append({'source': dump(i), 'target': dump(o), 'type': dump(p)})
    for o in g.objects(subject=i, predicate=rdflib.RDFS.label):
        triples.append({'source': dump(i), 'target': o, 'type': 'label'})

print json.dumps(triples, indent=0)
sys.exit(0)
