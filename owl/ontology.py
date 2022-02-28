from owlready2 import get_ontology

class Ontology():

    def __init__(self):
        self._template_onto = get_ontology("file://owl/ontologie.owl").load()
        self._foaf = self._template_onto.get_imported_ontologies().first().load()

    def _add_authors(self, authors, arxiv_document):
        
        for author in authors:
            with self._template_onto:
                
    def add_document(self, document):
        
       

    def add_named_entity(self, named_entity, arxiv_document):
        
       

    def save(self,filepath):
        
        self._template_onto.save(filepath)

