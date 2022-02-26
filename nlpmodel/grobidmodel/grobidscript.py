from grobid.client import GrobidClient
import sys 
print(sys.path)

client = GrobidClient("localhost","8070")
rsp = client.serve("processReferences","/home/guigui/Documents/KnowledgeGraph/nlpmodel/grobidmodel/test2.pdf", consolidate_header=1)