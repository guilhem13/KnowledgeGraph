import arxiv 
from models import Papier

class Data():

    count = 10 

    def __init__(self,count):
        self.count = count
    
    def get_doi(self,entry_doi):
        doi = entry_doi.split("/")[-1]
        return doi 

    def get_set_data(self):
        
        client_arxiv = arxiv.Client(page_size =self.count,delay_seconds = 3,num_retries = 5)
        paper_list= []
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =self.count,sort_by = arxiv.SortCriterion.SubmittedDate,)):
            paper_list.append(Papier(result.title,self.get_doi(result.entry_id),str(result.authors),result.pdf_url,result.summary))
        
        return paper_list
        
        
