class SA(object):



    def match(self,word,match):
        sf=[]
        for i in range(0,len(word)):
                sf.append(word[i:])
        testarray=[]
        for i in sf:
            if i.startswith(match):
                testarray.append([i])
        return testarray

    def findsort(self,word,match):
        array = self.match(word,match)
        str1=array[0]
        for x in array:
            if x<str1:
                str1 = x
        return str1

    def findlong(self,word,match):
        array = self.match(word,match)
        str1 = array[0]
        for x in array:
            if len(x)>len(str1):
                str1 = x
        return str1
