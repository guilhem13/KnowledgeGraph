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
            print(arxiv_data[i].link)
            a = str(arxiv_data[i].link).split("/")[-1]
            print(a)
            processor = Textprocessed(arxiv_data[i].link)
            arxiv_data[i].entities_include_in_text = processor.__getattr__()
            text_processed = processor.get_data_from_pdf()
            arxiv_data[i].entities = nltkmodel.nltktreelist(text_processed)
            #TODO faire la même chose qu'au dessus avec standford tagger 
            #TODO arxiv_data[i].subject 
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True
