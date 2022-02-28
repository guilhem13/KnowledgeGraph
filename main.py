from controller import Pipeline
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import multiprocessing as mp
from owl import ontology

def main_function():

    p = Pipeline("https://export.arxiv.org/pdf/",0)
    out_queue = mp.Queue()
    return p.make_traitement_pipeline(1, out_queue)

if __name__ == '__main__':
    
    papiers = main_function()
    owl = ontology.Ontology()
    for papier in papiers: 
        owl.add_papier(papier)
    owl.save('result.owl')
