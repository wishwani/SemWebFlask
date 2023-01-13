# Semantic Web Project

** Designed a calendar that follows the linked data principles **

**By**
- Sara Assefa ALEMAYEHU
- Randika Wishwani RATHWATHTHAGE

# Features

** Generating TURTEL file **
- "TTL_File_Generator.py" file is responsible to generate our RDF graph
* Installation 
  - $ pip install Calendar
  - $ pip install Flask
- Run the file and the out put .ttl file displayed in "http://localhost:5000/cadata"
- For windo os to see the ttl format ctrl+u
- for Mac os to see the ttl format ctr+option+u

** Posting the generated file **

- Creat LDP container https://territoire.emse.fr/ldp
- Give the link to the created container 
- run the code 
* In our case:
- Here we make a post by giving the container we created in Territoire LDP which is: https://territoire.emse.fr/ldp/sararandika2/ 
- It generate spesiffic UID for each event 
- User can take one given UID to look at specific event

** Query the graph **

- Query the graph is GET_EVENTS which uses a sparql query to fetch events occurring on a specific date (as specific by the user) from the LDP.
- Query an event 
  1 Get the first 10 subject,pridicate,object from our graph 
  2 Get the subject,pridicate,object from all graph 
  3 Get spesific course given the name of the course
  4 Get the up comming events


# Validation
* Installation
  -Install with PIP (Using the Python3 pip installer pip3)
   $ pip3 install pyshacl
- Or in a python virtualenv (these example commandline instructions are for a Linux/Unix based OS)
  - $ python3 -m virtualenv --python=python3 --no-site-packages .venv
  - $ source ./.venv/bin/activate
  - $ pip3 install pyshacl 

- To validte if the generated graph in a proper shape
- Use EVENT.ttl file as shacl_file 
- Give the generated calander graph
- Run the validate.py
