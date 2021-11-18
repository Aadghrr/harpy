import requests,json,os,sys
from src.filter import Filter

class HTTPArchiveFile():
    def __init__(self,HAR_FILE):
        self.har = self.loadFile(HAR_FILE)

    def loadFile(self,harFile):
        with open(harFile,'r') as f:
            har = json.loads(f.read())
        return har

    def schema(self,x,i=0):
        if type(x)==type(dict()) and len(x)!=0:
            for k in x:
                print(' '*i,'-'*i,k,sep='')
                self.schema(x[k],i+1)
        elif type(x)==type(list()) and len(x)>0:
            if type(x[0])==type(dict()) and len(x[0])!=0:
                print(' '*i,'L')
                self.schema(x[0],i)

    def getSchema(self):
        self.schema(self.har)

    def filter(self,*filters):
        filters = [Filter(filter) for filter in filters]
        msgs = enumerate(self.har['log']['entries'])
        msgs = [(i,msg) for i,msg in msgs if all([filter.decide(msg) for filter in filters])]
        return msgs

    def repeater(self,reqNum):
        req = self.har['log']['entries'][reqNum]['request']
        res = self.har['log']['entries'][reqNum]['response']
        print(req)
        url = req['url']
        headers = {x['name']:x['value'] for x in req['headers']}
        if 'postData' in req.keys():
            data =  {x['name']:x['value'] for x in req['postData']['params']}
        else:
            data=None
        print(url,headers,data)
        if req['method']=='GET':
           return requests.get(url,headers=headers)
        elif req['method']=='POST':
           return requests.get(url,headers=headers,data=data)

    def anomalies(self,msg=None):
        if msg==None: msg=enumerate(self.har['log']['entries'])

    def print(self,msg):
        pass
