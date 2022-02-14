from redis_om import HashModel

class Papier():

    title = None,
    authors = None,
    link = None,
    summary = None,
    entities_from_reference = None,
    entities_include_in_text = None, 
    subject = None
    url_in_text = None
    doi_in_text = None  

    def __init__(self,title,authors,link,summary):

        self.title = title,
        self.authors = authors,
        self.link = link,
        self.summary = summary
   


