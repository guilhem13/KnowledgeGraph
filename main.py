from controller import Pipeline
import nltk
import multiprocessing 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
def main ():
    pass

def main_function():

    p = Pipeline("https://export.arxiv.org/pdf/",0)
    #return p.multi_threading(5)
    import multiprocessing as mp
    out_queue = mp.Queue()
    return p.make_traitement_pipeline(out_queue)

if __name__ == '__main__':
    
    main_function()
    
