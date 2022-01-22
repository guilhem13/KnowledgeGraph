from controller import Pipeline
import nltk 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def main ():
    pass
  
if __name__ == '__main__':
    p= Pipeline("https://export.arxiv.org/pdf/")
    p.make_traitement_pipeline()
    main()