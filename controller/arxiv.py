import arxiv 
from models import Papier

class Data(): 

    def get_set_data():
        search = arxiv.Search(
            query = "computer science & ai",
            max_results = 10, 
            sort_by = arxiv.SortCriterion.SubmittedDate
        )
        paper_list= []
        for result in search.results():
            paper_list.append(Papier(result.title,str(result.authors),result.pdf_url,result.summary))

        return paper_list
        
        
