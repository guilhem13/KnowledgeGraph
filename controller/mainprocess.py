from pickle import TRUE
from unittest import result
from controller import Data , Textprocessed
from nlpmodel import nltkmodel , standfordnermodel ,spacymodel
from multiprocessing.pool import ThreadPool as Pool #TODO A enlever 
import json
import redis 
from multiprocessing import Process
import multiprocessing as mp


redis_host = "localhost"
redis_port = 6379


class Pipeline():

    start=None 

    def __init__(self,arxiv_url,start):
        self.arxiv_url = arxiv_url
        self.start =start
        pass
    
    def get_references(self, textprocessed): 

        nltkresult = nltkmodel.nltktreelist(textprocessed)["persons"]
        Standfordresult = standfordnermodel.get_continuous_chunks(textprocessed)["persons"]
        #spacyresult = spacymodel.spacylist(textprocessed)
        resultList= list(set(nltkresult) | set(Standfordresult))
        #resultList = list(set(resultList) | set(spacyresult))
        resultList = [x for x in nltkresult if len(x)>1 ]
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
        except Exception as e:
            print(e)
            print('error with item')
    #TODO 
    #https://docs.python.org/2/library/multiprocessing.html#using-a-pool-of-workers
    #https://stackoverflow.com/questions/15143837/how-to-multi-thread-an-operation-within-a-loop-in-python
    
    def multi_threading(self,pool_size):
        arxiv_data = Data.get_set_data(self.start)
        pool = Pool(pool_size)
        for item in arxiv_data:
            pool.apply_async(self.worker, (item,))
        pool.close()
        pool.join()
        f = open("test.json", "a")
        for i in range(len(arxiv_data)):
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True#arxiv_data"""

    """
    def make_traitement_pipeline(self): #https://export.arxiv.org/pdf/
        arxiv_data = Data.get_set_data(self.start)
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
    """
###########################################################################################################
    def multi_process(self, data, out_queue):         
        processor = Textprocessed(data.link[0])            
        text_processed = processor.get_data_from_pdf()
        data.entities_include_in_text = processor.find_entities_in_raw_text()
        data.entities_from_reference = self.get_references(text_processed)
        out_queue.put(data)

    def make_traitement_pipeline(self,out_queue): 
        arxiv_data = Data.get_set_data(self.start)
        workers = [ mp.Process(target=self.multi_process, args=(ele, out_queue) ) for ele in arxiv_data ]

        for work in workers: work.start()
        for work in workers: work.join(timeout=3)

        res_lst = []
        for j in range(len(workers)):
            res_lst.append(out_queue.get())

        f = open("test.json", "a")
        for test in res_lst: 
            f.write(json.dumps(test.__dict__))
        f.close()
     # TODO récolter le nombre de coeur pour ensuite le mettre sur le code
     # gérer le problème quand c'est 10000  

    out_queue = mp.Queue()

    