import arxiv 
from models import Papier , Entity

class Data():

    count = 10 

    def __init__(self,count):
        self.count = count
    
    def get_doi(self,entry_doi):
        doi = entry_doi.split("/")[-1]
        return doi 

    def process_authors(self,list_authors): 
        if len(list_authors) >0:
            result= []
            for i in range(len(list_authors)): 
                auteur = str(list_authors[i])
                seperate_name = auteur.split(" ")
                if len(seperate_name) >2:  # Prend en compte les noms du type David A. Strubbe
                    p = Entity()
                    p.set_prenom(str(seperate_name[0]+" "+seperate_name[1]))
                    p.set_nom(seperate_name[2])
                    result.append(p)
                else: 
                    p = Entity()   #TODO Faie un cas où ya que le nom par exemple    
                    p.set_prenom(seperate_name[0])
                    p.set_nom(seperate_name[1])
                    result.append(p)
            return result
        else: 
            print("No authors on this paper")
            return None 

    def get_set_data(self):
        
        client_arxiv = arxiv.Client(page_size =self.count,delay_seconds = 3,num_retries = 5)
        paper_list= []
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =self.count,sort_by = arxiv.SortCriterion.SubmittedDate,)):
            paper_list.append(Papier(result.title,self.get_doi(result.entry_id),self.process_authors(result.authors),result.pdf_url,result.summary,result.published))
        
        return paper_list
        
        
