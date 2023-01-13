from icalendar import Calendar
from rdflib import Graph, URIRef, Namespace, Literal, BNode


rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")


g = Graph()
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("schema", SCHEMA)

# schedule = URIRef("https://ci.mines-stetienne.fr/cps2/schedule/fdfsgfffsgg/")

#g.add((schedule, rdf.type, SCHEMA.Schedule))
#g.add(('hhhh667776544', rdf.type, SCHEMA.Schedule))

with open('ADECal.ics', 'r') as file:
    ecal = Calendar.from_ical(file.read())
    for component in ecal.walk():
     event = BNode()
     if component.name == "VEVENT":
        
        #g.add((schedule, SCHEMA.eventSchedule, event))
        g.add((event, SCHEMA.uid, Literal(component.get("uid"))))
        g.add((event, rdf.type, SCHEMA.Event))
        g.add((event, SCHEMA.name, Literal(component.get("summary"))))
        g.add((event, SCHEMA.location, Literal(component.get("location"))))
        g.add((event, SCHEMA.startDate, Literal(component.decoded("dtstart"))))       
        g.add((event, SCHEMA.endDate, Literal(component.decoded("dtend"))))
        g.add((event, SCHEMA.lecturer, Literal(component.decoded("DESCRIPTION"))))
        
  
        
    file.close()
print(g.serialize(r"/Users/sathish.bowatta/Documents/M2/iot/SemanticWeb/caloutput.ttl", format="ttl"))