import requests
from xml.etree.ElementTree import fromstring, ElementTree
from models import Entity

class Cermine():

    path = None

    def __init__(self,path):
        self.path = path
    
    def request_service(self, path): 

        headers = {'Content-Type': 'application/binary'}
        data = open(path, 'rb').read()
        response = requests.post('http://cermine.ceon.pl/extract.do', headers=headers, data=data)
        return response 
    
    def get_entities(self): 
        response = self.request_service(self.path)
        tree =  ElementTree(fromstring(response.content.decode("utf-8", errors="replace")))
        root = tree.getroot()
        result =[]
        for child in root.find("./back/ref-list"):
            for persons in child.findall('mixed-citation/string-name'):
                for person in persons:
                    p = Entity()
                    if person.tag == 'given-names':
                        p.set_prenom(person.text)
                    if person.tag =='surname': 
                        p.set_nom(person.text)
                    result.append(p)
                    
        return result
       