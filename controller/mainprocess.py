from pickle import TRUE
from unittest import result
from controller import Data , Textprocessed
from nlpmodel import nltkmodel , standfordnermodel ,spacymodel
from multiprocessing.pool import ThreadPool as Pool #TODO A enlever 
import json
import redis 
from multiprocessing import Process
import multiprocessing as mp
import urllib.request
import threading
from multiprocessing import cpu_count

redis_host = "localhost"
redis_port = 6379


class Pipeline():

    start=None 

    def __init__(self,arxiv_url,start):
        self.arxiv_url = arxiv_url
        self.start =start
        pass
    
    def get_references(self, textprocessed): #spacyresult = spacymodel.spacylist(textprocessed)

        nltkresult = nltkmodel.nltktreelist(textprocessed)["persons"]
        Standfordresult = standfordnermodel.get_continuous_chunks(textprocessed)["persons"]
        resultList= list(set(nltkresult) | set(Standfordresult))
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

###########################################################################################################
    def multi_process(self, data, out_queue):
        if urllib.request.urlopen("http://172.17.0.3:5000/"):
            print(data.link[0])       
            processor = Textprocessed(data.link[0])            
            text_processed = processor.get_data_from_pdf()
            data.entities_include_in_text = processor.find_entities_in_raw_text()
            data.entities_from_reference = self.get_references(text_processed)
            data.url_in_text = processor.find_url_in_text()
            data.doi_in_text = processor.find_doi_in_text()#frfr
            out_queue.put(data)

    
    def make_traitement_pipeline(self,out_queue): 
        arxiv_data = Data.get_set_data(self.start)
        res_lst = []
        f = open("test.json", "a")
        for i in range(0,len(arxiv_data),20):
            print(i)
            temp =arxiv_data[i:i+20]
            workers = [ mp.Process(target=self.multi_process, args=(ele, out_queue) ) for ele in temp]
            #s = threading.Semaphore(4)
            for work in workers:
                #with s:
                work.start()
            for work in workers: work.join(timeout=3)

            #res_lst = []
            for j in range(len(workers)):
                #res_lst.append(out_queue.get())
                f.write(json.dumps(out_queue.get().__dict__))

        #for test in res_lst: 
        #   f.write(json.dumps(test.__dict__))
        f.close()
     # TODO récolter le nombre de coeur pour ensuite le mettre sur le code
     # gérer le problème quand c'est 10000  
     #https://blog.ruanbekker.com/blog/2019/02/19/parallel-processing-with-python-and-multiprocessing-using-queue/
     #https://towardsdatascience.com/pool-limited-queue-processing-in-python-2d02555b57dc

    

    