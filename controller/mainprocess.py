from pickle import TRUE
from unittest import result
from controller import Data , Textprocessed
from nlpmodel import nltkmodel , standfordnermodel
from multiprocessing.pool import ThreadPool as Pool
import json
import redis 

redis_host = "localhost"
redis_port = 6379


class Pipeline(): 

    def __init__(self,arxiv_url):
        self.arxiv_url = arxiv_url
        pass
    
    def get_references(self, textprocessed): 

        nltkresult = nltkmodel.nltktreelist(textprocessed)["persons"]
        Standfordresult = standfordnermodel.get_continuous_chunks(textprocessed)["persons"]
        resultList= list(set(nltkresult) | set(Standfordresult))
        resultList = [x for x in resultList if len(x)>1 ]
        #return nltkresult
        return resultList

        #TODO A voir les modèles ne marche pas 
    def redis_string(self):
        try: 
            r = redis.StrictRedis(host = redis_host,port = redis_port, decode_responses=True)
            r.set("message","Hello_World")
            msg =r.get("message")
            print(msg)
        except Exception as e: 
            print(e)

    def worker(self, item):
        try:
            processor = Textprocessed(item.link[0])            
            text_processed = processor.get_data_from_pdf()
            item.entities_include_in_text = processor.find_entities_in_raw_text()
            item.entities_from_reference = self.get_references(text_processed)
        except:
            print('error with item')
    
    def multi_threading(self,pool_size):
        arxiv_data = Data.get_set_data()
        pool = Pool(pool_size)
        for item in arxiv_data:
            pool.apply_async(self.worker, (item,))
        pool.close()
        pool.join()
        f = open("test.json", "a")
        for i in range(len(arxiv_data)):
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True#arxiv_data

    def make_traitement_pipeline(self): #https://export.arxiv.org/pdf/
        arxiv_data = Data.get_set_data()
        f = open("test.json", "a")
        for i in range(len(arxiv_data)):
            processor = Textprocessed(arxiv_data[i].link[0])            
            text_processed = processor.get_data_from_pdf()
            arxiv_data[i].entities_include_in_text = processor.find_entities_in_raw_text()
            arxiv_data[i].entities_from_reference = self.get_references(text_processed)
            #TODO arxiv_data[i].subject 
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True

#TODO faire le multi threading https://ichi.pro/fr/multithreading-en-python-et-comment-y-parvenir-28270357503503
#https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python#:~:text=Multithreading%20(sometimes%20simply%20%22threading%22,a%20thread%20to%20be%20completed.