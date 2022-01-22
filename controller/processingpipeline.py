import unicodedata
import re 
import pdfx

class Textprocessed(): 
    url = None
    raw_text =None

    def __init__(self,url):
        self.url =url

    def get_references_part(self,Pdf_Readed):
        result=""
        temp = unicodedata.normalize('NFKD',Pdf_Readed).encode('ascii','ignore').decode('unicode_escape').encode('ascii','ignore').decode()
        keyword_list = ['\nReferences\n', '\nREFERENCES\n','\nreferences\n']
        keyword = [ele for ele in keyword_list if(ele in temp)]
        if keyword != None:
            if len(keyword) == 1: 
                keyword = str(keyword[0]) 
                index = temp.index(keyword) # check ici parcequ'il y a plusieurs versions de références 
                result = temp[index +len(keyword):]
                return result
            else: 
                return "erreur problème: Plusieurs références ! " #TODO enlever cette partie non disruptive 

    def clean_references_part(self,data):
        temp = re.sub(' +', ' ', data)
        temp = temp.replace("-\n", "") # reconstruire les retours à la ligne 
        temp = temp.replace("\n"," ") #rajout d'espace 
        return temp

    def get_data_from_pdf(self):

        ##
        pdf = pdfx.PDFx(self.url)
        metadata = pdf.get_metadata()
        references_list = pdf.get_references()
        references_dict = pdf.get_references_as_dict()
        ###
        textfrompdf = pdf.get_text()
        self.raw_text = textfrompdf
        textfrompdf = self.clean_references_part(self.get_references_part(textfrompdf))
        return textfrompdf

    def __getattr__(self):
        return self.raw_text
        
    