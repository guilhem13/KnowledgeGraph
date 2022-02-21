files = {'upload_file': open('file.txt','rb')}
values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

r = requests.post(url, files=files, data=values)