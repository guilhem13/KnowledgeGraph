import arxiv 
from models import Papier

class Data(): 

    def get_set_data():

        #http://lukasschwab.me/arxiv.py/index.html
        client_arxiv = arxiv.Client(page_size =4000,delay_seconds = 3,num_retries = 5)
        paper_list= []
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =10,sort_by = arxiv.SortCriterion.SubmittedDate,)):
            paper_list.append(Papier(result.title,str(result.authors),result.pdf_url,result.summary))
        
        return paper_list

        """
        client_arxiv = arxiv.Client(page_size =4000,delay_seconds = 3,num_retries = 5)
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =float('inf'),sort_by = arxiv.SortCriterion.SubmittedDate,)):
            Papier(result.title,str(result.authors),result.pdf_url,result.summary,"","","").save()
        
        """
        
        
