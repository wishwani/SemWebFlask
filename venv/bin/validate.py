
from pyshacl import validate
from rdflib import Graph

shacl_file = '/Users/sathish.bowatta/Desktop/SemWebFlask/venv/bin/EVENT.ttl'
data_graph = '/Users/sathish.bowatta/Desktop/SemWebFlask/venv/bin/caloutput.ttl'



if __name__ == "__main__":
    #d = Graph().parse(data=data_graph, format="turtle")
    #s = Graph().parse(data=shacl_file, format="turtle")
    conforms, report, message = validate(data_graph, shacl_file, advanced=True, debug=False)
    print(message)