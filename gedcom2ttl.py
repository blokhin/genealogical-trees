#!/usr/bin/env python

# This script converts GEDCOM genealogy members
# to the FHKB turtle semantic web ontology individuals.
# (A header with FHKB ontology definitions is still required.)
# TODO adoptive families (>1) are not considered (TODO?)
# Author: Evgeny Blokhin
# License: MIT

import os, sys
from gedcom import Gedcom


try: workpath = sys.argv[1]
except IndexError: sys.exit("No gedcom defined!")

def term2id(el):
    return "i" + el.pointer().replace('@', '').lower()

g = Gedcom(workpath)
gedcom_dict = g.element_dict()
individuals, marriages = {}, {}

for k, v in gedcom_dict.iteritems():
    if v.is_individual():
        children, siblings = set(), set()
        idx = term2id(v)

        title = v.name()[0].decode('utf8').encode('ascii', 'xmlcharrefreplace') + " " + v.name()[1].decode('utf8').encode('ascii', 'xmlcharrefreplace')
        title = title.replace('"', '').replace('[', '').replace(']', '').replace('(', '').replace(')', '').strip()

        own_families = g.families(v, 'FAMS')
        for fam in own_families:
            children |= set(term2id(i) for i in g.get_family_members(fam, "CHIL"))

        parent_families = g.families(v, 'FAMC')
        if len(parent_families):
            for member in g.get_family_members(parent_families[0], "CHIL"): # NB adoptive families i.e len(parent_families)>1 are not considered (TODO?)
                if member.pointer() == v.pointer():
                    continue
                siblings.add(term2id(member))

        if idx in individuals:
            children |= individuals[idx].get('children', set())
            siblings |= individuals[idx].get('siblings', set())
        individuals[idx] = {'sex': v.gender().lower(), 'children': children, 'siblings': siblings, 'title': title}

    elif v.is_family():
        wife, husb, children = None, None, set()
        children = set(term2id(i) for i in g.get_family_members(v, "CHIL"))

        try:
            wife = g.get_family_members(v, "WIFE")[0]
            wife = term2id(wife)
            if wife in individuals: individuals[wife]['children'] |= children
            else: individuals[wife] = {'children': children}
        except IndexError: pass
        try:
            husb = g.get_family_members(v, "HUSB")[0]
            husb = term2id(husb)
            if husb in individuals: individuals[husb]['children'] |= children
            else: individuals[husb] = {'children': children}
        except IndexError: pass

        if wife and husb: marriages[wife + husb] = (term2id(v), wife, husb)

for idx, val in individuals.iteritems():
    added_terms = ''
    if val['sex'] == 'f':
        parent_predicate, sibl_predicate = "isMotherOf", "isSisterOf"
    else:
        parent_predicate, sibl_predicate = "isFatherOf", "isBrotherOf"
    if len(val['children']):
        added_terms += " ;\n    fhkb:" + parent_predicate + " " + ", ".join(["fhkb:" + i for i in val['children']])
    if len(val['siblings']):
        added_terms += " ;\n    fhkb:" + sibl_predicate + " " + ", ".join(["fhkb:" + i for i in val['siblings']])
    print "fhkb:%s a owl:NamedIndividual, owl:Thing%s ;\n    rdfs:label \"%s\" .\n" % (idx, added_terms, val['title'])

for k, v in marriages.iteritems():
    print "fhkb:%s a owl:NamedIndividual, owl:Thing ;\n    fhkb:hasFemalePartner fhkb:%s ;\n    fhkb:hasMalePartner fhkb:%s .\n" % v

print "[] a owl:AllDifferent ;\n    owl:distinctMembers ("
for idx in individuals.keys():
    print "    fhkb:" + idx
for k, v in marriages.iteritems():
    print "    fhkb:" + v[0]
print "    ) ."
