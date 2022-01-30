from controller import Pipeline
import nltk
import multiprocessing 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
def main ():
    pass

def main_function():

    
    Base_Url_Query = 'http://export.arxiv.org/api/query?'
    search_query = 'cat:cs.AI'
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query,0,1)
    response =  urllib.request.urlopen(Base_Url_Query+query).read()
    tree = ElementTree(fromstring(response))
    root = tree.getroot()
    totalresults = root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults").text
    print("Total_results :"+str(totalresults))
    totalresults ="3999"
    start = 0
    while start < int(totalresults): 
        Pipeline("https://export.arxiv.org/pdf/",start).multi_threading(5)
        start += 4000
    #return p.multi_threading(5)
    #return p.make_traitement_pipeline()

if __name__ == '__main__':
    
    main_function()
    
