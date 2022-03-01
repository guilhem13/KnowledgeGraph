from controller import Pipeline
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import multiprocessing as mp
from owl import ontology
from controller import Data

def main_function(block_paper):

    p = Pipeline("https://export.arxiv.org/pdf/",0)
    out_queue = mp.Queue()
    batch_size = 5
    return p.make_traitement_pipeline(block_paper, out_queue, batch_size)

if __name__ == '__main__':

    nb_paper_to_request = 15
    block_arxiv_size = 5
    arxiv_data = Data(nb_paper_to_request).get_set_data()
    papiers= []
    for i in range(0,len(arxiv_data),block_arxiv_size):
        print(i) 
        papiers+= main_function(arxiv_data[i:i+block_arxiv_size])
    #papiers = main_function()
    owl = ontology.Ontology()
    for papier in papiers: 
        owl.add_papier(papier)
    owl.save('result.owl')
