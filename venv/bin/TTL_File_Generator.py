from icalendar import Calendar
from rdflib import Graph, URIRef, Namespace, Literal, BNode, URIRef
from flask import Flask, request
import re


app = Flask(__name__)


@app.route('/cadata', methods=['GET'])
def convertto_RDF():
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    SCHEMA = Namespace("https://schema.org/")
    ldp = Namespace("http://www.w3.org/ns/ldp#")

    g = Graph()
    g.bind("rdf", rdf)
    g.bind("rdfs", rdfs)
    g.bind("schema", SCHEMA)
    g.bind("ldp", ldp)

    schedule = URIRef("https://territoire.emse.fr/ldp/sararandika2/")

    with open('C://CPS2-M2//Semantic-Web//Project/SemWebFlask/venv/bin/ADECal.ics', 'r') as f:
        ecal = Calendar.from_ical(f.read())
        for component in ecal.walk():
            event = (Literal(component.get("uid")))
            if component.name == "VEVENT":

                g.add((URIRef(event), rdf.type, SCHEMA.Event))
                g.add((URIRef(event), SCHEMA.uid, Literal(component.get("uid"))))
                g.add((URIRef(event), SCHEMA.name,
                      Literal(component.get("summary"))))
                g.add((URIRef(event), SCHEMA.location,
                      Literal(component.get("location"))))
                g.add((URIRef(event), SCHEMA.startDate,
                      Literal(component.decoded("dtstart"))))
                g.add((URIRef(event), SCHEMA.endDate,
                      Literal(component.decoded("dtend"))))
                g.add((URIRef(event), SCHEMA.lecturer, Literal(
                    component.decoded("DESCRIPTION"))))
        f.close()
        print(g.serialize(
            r"C:/CPS2-M2/Semantic-Web/Project", format="ttl"))

    return(g.serialize(format="ttl"))


app.run(host='localhost', port=5000)

if __name__ == "_main_":
    app.run(debug=True)
