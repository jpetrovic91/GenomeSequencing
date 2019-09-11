from random import choice

class pairedDeBruijnGraph:        
    def __init__(self,L,k,d):
        self.edges=L
        self.k=k
        self.d=d

    def createPaths(self,startNode):
        paths={}
        count=0
        for edge in self.edges:
            prefix=edge[:self.k-1]+self.d*'_'+edge[self.k+self.d:-1]
            suffix=edge[1:self.k]+self.d*'_'+edge[self.k+self.d+1:]
            if prefix in paths.keys():
                paths[prefix].append(suffix)
            else:
                paths[prefix]=[suffix]
            count+=1
        endNode=self.edges[-1][1:self.k]+self.d*'_'+self.edges[-1][self.k+self.d+1:]
        if endNode in paths.keys():
            paths[endNode].append(startNode)
        else:
            paths[endNode]=[startNode]
        count+=1
        
        return (paths,count)
    
    def EulerianCycle(self):
        startNode=self.edges[0][:self.k-1]+self.d*'_'+self.edges[0][self.k+self.d:-1]
        
        (allPaths,count)=self.createPaths(startNode)
        
        path=[startNode]
        pathNode=startNode
        while allPaths[pathNode]!=[]:
            nextNode=choice(allPaths[pathNode])
            allPaths[pathNode].remove(nextNode)
            pathNode=nextNode
            path.append(pathNode)
            count-=1
        path.pop()
    
        newStartNode=None 
        while count!=0:
            for node in path:
                if allPaths[node]!=[]:
                    newStartNode=node
                    break
        
            if newStartNode==None:
                return False
               
            path=rotateList(path,path.index(newStartNode))
            path.append(newStartNode)
    
            pathNode=newStartNode
            while allPaths[pathNode]!=[]:
                nextNode=choice(allPaths[pathNode])
                allPaths[pathNode].remove(nextNode)
                pathNode=nextNode
                path.append(pathNode)  
                count-=1
            path.pop()
             
        path=rotateList(path,path.index(startNode))
        return path

def createPairedDeBruijn(kmersList,k,d):
    return pairedDeBruijnGraph(kmersList,k,d)

def rotateList(List,n):
    return List[n:]+List[:n]

def createPairedKmerList(data,k,d):
    L=[]
    for i in range(len(data)-(2*k+d)+1):
        L.append(data[i:k+i]+d*'_'+data[k+d+i:2*k+d+i])
    return L

def Genome(path,k,d):
    prefixString=path[0][:k-1]
    suffixString=path[0][k+d-1:]
    
    for i in range(1,len(path)):
        prefixString+=path[i][k-2]
        suffixString+=path[i][-1]

    isValid=False
    if prefixString[k+d:]==suffixString[:-(k+d)]:
        isValid=True
    
    genome=prefixString+suffixString[-(k+d):]

    return genome,isValid

def compareStrings(string1,string2):
    counter=0
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            counter+=1
    return counter    

if __name__=='__main__':
    
    with open("full_genome.txt") as file:
        data=file.read()
    data=data.replace('\n','')
    k,d=[int(i) for i in input().split()]
    L=createPairedKmerList(data,k,d)
    stringDifferences=[]
    countViables=0
    for i in range(100):
        G=createPairedDeBruijn(L,k,d)
        path=G.EulerianCycle()
        finalGenome,isValid=Genome(path,k,d)
        if isValid:
            countViables+=1
        diff=compareStrings(finalGenome,data)
        stringDifferences.append(diff)
    count=0
    countZeros=0
    for i in stringDifferences:
        count+=i
        if i==0:
            countZeros+=1
    print(count/100)
    print(countViables)
    print(countZeros)
