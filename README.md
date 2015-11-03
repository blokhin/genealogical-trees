Semantic Web Genealogical Trees
======

This is an example of logical reasoning applied to the graphs of genealogical trees. Defining the kinship types on top of genealogical trees is the perfect use case for semantic technologies.

The source of data is the GEDCOM file format common for exchange of genealogical information. With the aid of **RDFLib** and **gedcom** Python libraries GEDCOM files are converted into the OWL 2 ontologies in Turtle syntax (**.ttl** file extension), adopting the conventions laid by Family History Knowledge Base ([FHKB](http://ceur-ws.org/Vol-1207/paper_11.pdf), see **data/header.ttl** file). Note that the FHKB ontology is although very small but uses unusually complex role hierarchy and is rather hard for modern reasoners. After reasoning with the naive Python implementation of the OWL 2 RL Profile and inferring all possible triples the ontologies are finally converted to JSON-formatted graphs for in-browser visualization. This is done inside the bundled **index.html** web-app by means of **D3.js** JavaScript library.

The above is summarized in the ```gedcom2json.sh``` script:

```shell
./gedcom2json.sh path/to/your/gedcom.ged path/to/entailed_graph.json
```

Resulting file ```entailed_graph.json``` is to be uploaded and visualized in the bundled web-app (no server scripting is used). It is currently hosted at GitHub: [http://blokhin.github.io/genealogical-trees](http://blokhin.github.io/genealogical-trees)

Note the following comment from FHKB authors:

> We probably do not wish to drive a genealogical application using an FHKB in this form. Its purpose is educational. It touches most of OWL 2 and shows a lot of what it can do, but also a considerable amount of what it cannot do.
> As inference is maximised, the FHKB breaks most of the OWL 2 reasoners at the time of writing. However, it serves its role to teach about OWL 2.
> OWL 2 on its own and using it in this style, really does not work for family history.

Reasoning with the naive Python implementation of the OWL 2 RL Profile is very slow and takes hours for relatively big family trees. Therefore use of the fast native reasoner (like Fact++) is very desirable. Wrapped in the [owl-cpp](http://owl-cpp.sourceforge.net) Python bindings, Fact++ performs up to two orders of magnitude faster.
