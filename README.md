Semantic Web Genealogical Trees
======

This is an example of logical reasoning applied to the graphs of genealogical trees. Defining the kinship types on top of these graphs is the perfect use case for semantic technologies.

The source of data is the GEDCOM format common for exchange of genealogical information. With the aid of **RDFLib** and **gedcom** Python libraries GEDCOM files are converted into the OWL 2 ontologies in Turtle syntax (**.ttl** file extension), adopting the conventions laid by Family History Knowledge Base ([FHKB](http://ceur-ws.org/Vol-1207/paper_11.pdf), see **data/header.ttl** file). After reasoning with the naive Python implementation of the OWL 2 RL Profile and inferring all possible triples the ontologies are finally converted to JSON-formatted graphs for in-browser visualization. This is done inside the bundled **index.html** web-app by means of **D3.js** JavaScript library.

The above is summarized as follows:

```shell
cp data/header.ttl data/new_example.ttl
./gedcom2ttl.py path/to/your/gedcom.ged >> data/new_example.ttl
./infer.py data/new_example.ttl
./ttl2json.py data/new_example.ttl.inferred > new_example.json
```

Resulting file **new_example.json** is to be uploaded and visualized in the bundled web-app (no server scripting is used). It is currently hosted at GitHub: [http://blokhin.github.io/genealogical-trees](http://blokhin.github.io/genealogical-trees)
