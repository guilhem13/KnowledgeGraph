from controller import Pipeline
import nltk
import multiprocessing 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def main ():
    pass

def main_function():
    p= Pipeline("https://export.arxiv.org/pdf/")
    return p.make_traitement_pipeline()

if __name__ == '__main__':
    #p = multiprocessing.Process(target=main_function())
    #p.start()
    #p.join()
    main_function()