import arxiv 
from models import Papier

class Data(): 

    def get_set_data():
        #http://lukasschwab.me/arxiv.py/index.html
        client_arxiv = arxiv.Client(page_size = 1000,delay_seconds = 3,num_retries = 5)
        """search = arxiv.Search(
            query = "computer science & ai",
            max_results = 10, 
            sort_by = arxiv.SortCriterion.SubmittedDate
        )
        paper_list= []
        for result in search.results():
            paper_list.append(Papier(result.title,str(result.authors),result.pdf_url,result.summary))

        return paper_list"""
        paper_list= []
        for result in client_arxiv.results(arxiv.Search(query = "computer science & ai",max_results =float('inf'),sort_by = arxiv.SortCriterion.SubmittedDate,)):
            paper_list.append(Papier(result.title,str(result.authors),result.pdf_url,result.summary))
        
        return paper_list

        
        
