#!/usr/bin/env python

import os, sys
import time

import rdflib

from RDFClosure import DeductiveClosure, OWLRL_Extension


try: workpath = sys.argv[1]
except IndexError: sys.exit("No path defined!")
try: recursion_limit = int(sys.argv[2])
except IndexError: recursion_limit = 0

if recursion_limit > 0: sys.setrecursionlimit(recursion_limit)

g = rdflib.Graph()
g.parse(workpath, format="turtle")

print "Recursion stack limit:", sys.getrecursionlimit()
print "Triples before:", len(g)
starttime = time.time()
DeductiveClosure(OWLRL_Extension).expand(g)
print "Done in %1.2f sc" % (time.time() - starttime)
print "Triples after:", len(g)

f = open(workpath + ".inferred", "w")
f.write(g.serialize(format="turtle"))
f.close()
sys.exit(0)
