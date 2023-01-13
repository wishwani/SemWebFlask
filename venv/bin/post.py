import requests
from rdflib import Graph, RDF, Namespace, Literal, URIRef, XSD

url = 'https://territoire.emse.fr/ldp/sararandika2/'

graph_name = 'caloutput.ttl'
username = "ldpuser"
password = "LinkedDataIsGreat"

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")

g = Graph().parse("C://CPS2-M2//Semantic-Web//Project/SemWebFlask/venv/bin/cal_ttl")
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("schema", SCHEMA)

for event in g.subjects(rdf.type, SCHEMA.Event):

    startDate = g.value(event, SCHEMA.startDate)
    endDate = g.value(event, SCHEMA.endDate)
    location = g.value(event, SCHEMA.location)
    lecturer = g.value(event, SCHEMA.lecturer)
    uid = g.value(event, SCHEMA.uid)
    name = g.value(event, SCHEMA.name)

    schedule_url = "/".format(uid)
    event = URIRef(schedule_url)

    graph = Graph()

    graph.add((event, rdf.type, SCHEMA.Event))
    graph.add((event, SCHEMA.uid, Literal(uid)))
    graph.add((event, SCHEMA.startDate, Literal(startDate)))
    graph.add((event, SCHEMA.endDate, Literal(endDate)))
    graph.add((event, SCHEMA.location, Literal(location)))
    graph.add((event, SCHEMA.lecturer, Literal(lecturer, datatype=XSD.string)))
    graph.add((event, SCHEMA.name, Literal(name)))

    headers = {
        'Content-type': 'text/turtle',
    }

    event = graph.serialize()

    params = {'graph': graph_name}
    response = requests.post(url, headers=headers,  auth=(
        username, password), params=params, data=event)
