class Filter():
    def __init__(self,filter):
        self.filter = filter.split('.')
        self.comparator=self.filter[-1]
        self.fields=self.filter[:-1]

    def decide(self,msg):
        str1 = self.resolve(msg)
        if not '*' in self.comparator:
            return self.equals(str1,self.comparator)
        elif self.comparator[0]=='*' and self.comparator[-1]=='*':
            return self.finds(str1,self.comparator[1:-1])

    def equals(self,str1,str2):
        return str1==str2

    def finds(self,str1,comparator):
        return comparator in str1

    def resolve(self,msg,i=0):
        if type(msg)!=type(dict()):
            return str(msg)
        else:
            msg = msg[self.filter[i]]
            return self.resolve(msg,i+1)
