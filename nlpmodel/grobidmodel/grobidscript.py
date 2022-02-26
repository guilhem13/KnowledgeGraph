from grobid.client import GrobidClient

client = GrobidClient("localhost","8070")
rsp = client.serve("processReferences","test2.pdf", consolidate_header=1)