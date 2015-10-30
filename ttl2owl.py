#!/usr/bin/env python
'''
NB / TODO
The ontologies generated with this script have 2 issues:
(1)
missing IRI, e.g. the following may be used
<owl:Ontology rdf:about="">
<owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Lorem ipsum dolor sit amet, consectetur, adipisci velit, ...</owl:versionInfo>
</owl:Ontology>

(2)
non-standard node attribute:
 rdf:nodeID="(\w*)"
must be removed
'''
import sys
import rdflib


try: workpath = sys.argv[1]
except IndexError: sys.exit("No path defined!")
try: recursion_limit = int(sys.argv[2])
except IndexError: recursion_limit = 0

if recursion_limit > 0: sys.setrecursionlimit(recursion_limit)

g = rdflib.Graph()
g.parse(workpath, format="turtle")

f = open(workpath + ".owl", "w")
f.write(g.serialize(format="pretty-xml"))
f.close()
sys.exit(0)
