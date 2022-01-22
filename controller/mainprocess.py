from pickle import TRUE
from controller import Data , Textprocessed
from nlpmodel import nltkmodel
import json 

class Pipeline(): 

    def __init__(self,arxiv_url):
        self.arxiv_url = arxiv_url
        pass

    def make_traitement_pipeline(self): #https://export.arxiv.org/pdf/
        arxiv_data = Data.get_set_data()
        f = open("test.json", "a")
        for i in range(len(arxiv_data)):
            #print(arxiv_data[i].link)
            #TODO régler le problème avec ('http://arxiv.org/pdf/2201.08383v1',) c'est un tuple et pas un string 
            #a = str(arxiv_data[i].link).split("/")[-1]
            #print(a)

            #processor = Textprocessed(arxiv_data[i].link)
            processor = Textprocessed(arxiv_data[i].link[0])            
            text_processed = processor.get_data_from_pdf()
            arxiv_data[i].entities_include_in_text = processor.find_entities_in_raw_text()
            arxiv_data[i].entities_from_reference = nltkmodel.nltktreelist(text_processed)
            #TODO faire la même chose qu'au dessus avec standford tagger 
            #TODO arxiv_data[i].subject 
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True
