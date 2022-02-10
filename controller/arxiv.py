import arxiv 
from models import Papier
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
from bs4 import BeautifulSoup

class Data(): 

    def get_set_data(start):
        """Base_Url ="https://arxiv.org"
        #template = "https://arxiv.org/pdf/cs/" #TODO faire une liste de template pour que ça marche sinon trop ou sinon passer par ARxvi.search 
        paper_list= []
        max_results = 10#00
        page = urllib.request.urlopen('https://export.arxiv.org/api/query?search_query=cat:cs.AI&start='+str(start)+'&max_results='+str(max_results))
        s = page.read()
        tree = ElementTree(fromstring(s))
        root = tree.getroot()
        for child in root:
            Auteurs =[]
            if (child.tag == "{http://www.w3.org/2005/Atom}entry"):
                Id_papier = child[0].text #template + child[0].text.split("/")[-1] +str(".pdf")
                Update = child[1].text
                Published = child[2].text
                Title = child[3].text
                Summary = child[4].text
                for child_sec in child[4:]:
                    if child_sec.tag == "{http://www.w3.org/2005/Atom}author":
                        if len(child_sec.getchildren()) ==2:
                            dictionnaire ={}
                            dictionnaire["Auteur"] = child_sec[0].text
                            dictionnaire["Affiliation"] = child_sec[1].text
                            Auteurs.append(dictionnaire)
                        else: 
                            Auteurs.append(child_sec[0].text)
                page2 =  urllib.request.urlopen(Id_papier).read()
                soup = BeautifulSoup(page2, 'html.parser')
                if soup.find('a', class_='abs-button download-pdf'): 
                    Papier_id = Base_Url+ soup.find('a', class_='abs-button download-pdf').get('href') + ".pdf" 
                    paper_list.append(Papier(Title,Auteurs, Papier_id,Summary))

        print(len(paper_list))
        return paper_list

        """
        #http://lukasschwab.me/arxiv.py/index.html
        client_arxiv = arxiv.Client(page_size =100,delay_seconds = 3,num_retries = 5)
        paper_list= []
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =100,sort_by = arxiv.SortCriterion.SubmittedDate,)):
            paper_list.append(Papier(result.title,str(result.authors),result.pdf_url,result.summary))
        
        return paper_list


        #arxiv.Search(id_list=["2202.03099v1"])):
        """
        #TODO for redis 
        
        client_arxiv = arxiv.Client(page_size =4000,delay_seconds = 3,num_retries = 5)
        for result in client_arxiv.results(arxiv.Search(query = "cat:cs.AI",max_results =float('inf'),sort_by = arxiv.SortCriterion.SubmittedDate,)):
            Papier(result.title,str(result.authors),result.pdf_url,result.summary,"","","").save()
        
        """
        
        
