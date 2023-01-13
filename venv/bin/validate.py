
from pyshacl import validate
from rdflib import Graph

shacl_file = 'C://CPS2-M2//Semantic-Web//Project/SemWebFlask/venv/bin/EVENT.ttl'
data_graph = 'C://CPS2-M2/Semantic-Web/Project/SemWebFlask/venv/bin/cal_ttl'


if __name__ == "__main__":
    conforms, report, message = validate(
        data_graph, shacl_file, advanced=True, debug=False)
    print(message)
