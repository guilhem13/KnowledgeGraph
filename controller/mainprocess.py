from controller import Data , Textprocessed
from nlpmodel import nltktreelist

class Pipeline(): 

    def __init__(self,arxiv_url):
        self.arxiv_url = arxiv_url
        pass

    def make_traitement_pipeline(self): #https://export.arxiv.org/pdf/
        arxiv_data = Data.get_set_data()
        for i in range(len(arxiv_data)):
            processor = Textprocessed(arxiv_data[i].link)
            arxiv_data[i].entities_include_in_text = processor.__getattr__()
            text_processed = processor.get_data_from_pdf()
            arxiv_data[i].entities = nltktreelist(text_processed)
            #TODO faire la même chose qu'au dessus avec standford tagger 
            #TODO arxiv_data[i].subject 
        

