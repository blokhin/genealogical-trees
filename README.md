Semantic Web Genealogical Trees
======
[![DOI](https://zenodo.org/badge/18811/blokhin/genealogical-trees.svg)](https://zenodo.org/badge/latestdoi/18811/blokhin/genealogical-trees)

Rationale
------

This is an example of logical reasoning applied to the graphs of genealogical trees. Defining the kinship types on top of genealogical trees seems to be the perfect use case for semantic technologies.

The source of data is the GEDCOM file format (**.ged**) common for exchange of genealogical information. With the aid of **RDFLib** and **gedcom** Python libraries GEDCOM files are converted into the OWL 2 ontologies (ABox) in Turtle syntax (**.ttl** file extension), adopting the TBox of the Family History Knowledge Base ([FHKB](http://ceur-ws.org/Vol-1207/paper_11.pdf), see ```data/header.ttl``` file). Note that the FHKB ontology is although very small but uses unusually complex role hierarchy and is rather hard for modern reasoners. After reasoning with the naive Python implementation of the OWL 2 RL Profile and inferring all possible triples the ontologies are finally converted to the JSON-formatted graphs for in-browser visualization. This is done inside the bundled ```index.html``` HTML5 web-app by means of **D3.js** JavaScript library.

Using this repository
------

The above is summarized in the ```gedcom2json.sh``` script, which is used like this:

```shell
./gedcom2json.sh path/to/your/gedcom.ged path/to/entailed_graph.json
```

Resulting file ```entailed_graph.json``` is to be uploaded and visualized in the bundled HTML5 web-app ```index.html``` (no server scripting is used). Its copy is currently hosted at GitHub: [http://blokhin.github.io/genealogical-trees](http://blokhin.github.io/genealogical-trees). Locally it should be served from a web-server (e.g. ```python -m SimpleHTTPServer``` or ```php -S localhost:8000```).

Before processing, the required Python libraries listed in ```requirements.txt``` should be installed (virtualenv is highly recommended).

Blog tutorial
------

https://blog.tilde.pro/semantic-web-technologies-on-an-example-of-family-trees-7518f3f835a9

Remark on FHKB
------

Note however the [following comment](http://www.researchgate.net/publication/271131820_Manchester_Family_History_Advanced_OWL_Tutorial) from FHKB authors:

> We probably do not wish to drive a genealogical application using an FHKB in this form. Its purpose is educational. It touches most of OWL 2 and shows a lot of what it can do, but also a considerable amount of what it cannot do.
> As inference is maximised, the FHKB breaks most of the OWL 2 reasoners at the time of writing. However, it serves its role to teach about OWL 2.
> OWL 2 on its own and using it in this style, really does not work for family history.

Remark on reasoning
------

Reasoning with the naive Python implementation of the OWL 2 RL Profile is very slow and takes hours for relatively big family trees. Therefore use of the fast native reasoner (like Fact++) is very desirable. Wrapped in the [owl-cpp](http://owl-cpp.sourceforge.net) Python bindings, Fact++ performs up to two orders of magnitude faster.
