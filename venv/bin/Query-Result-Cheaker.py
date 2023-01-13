from flask import Flask, render_template, url_for, request, flash, redirect
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph


sparql = SPARQLWrapper("https://territoire.emse.fr/ldp/")
sparql.setReturnFormat(JSON)
sparql.setCredentials("ldpuser", "LinkedDataIsGreat")

##### get the first 10 subject,pridicate,object from our graph ######
# sparql.setQuery("""
#             SELECT * FROM <https://territoire.emse.fr/ldp/sararandika2/>
#             WHERE { ?subj ?pre ?ob.
#                     }

#             LIMIT 10
#             """
#                 )

# sparql.setQuery("""
#             Select * {?subj a <https://schema.org/Event>;
#             <https://schema.org/startDate> ?startDate;
#             <https://schema.org/endDate> ?endDate;
#             <https://schema.org/location> ?location.} ORDER BY ASC(?startDate)
#             """
#                 )

######## get spesific course given the name of the course ###########
# sparql.setQuery("""

#             SELECT *
#             WHERE { ?sub ?name "CM/TD Programming connected devices / Digital Twins".
#                     }
#             LIMIT 10


#             """
#                 )

sparql.setQuery("""
    PREFIX schema: <http://schema.org/>
    SELECT ?event ?start 
    WHERE {
        ?event a schema:Event ;
               schema:startDate ?start .
        FILTER (?start >= NOW())
    }

    """
                )

try:
    qres = sparql.queryAndConvert()

    for r in qres["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
