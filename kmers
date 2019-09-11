from random import choice

class deBruijnGraph:        
    def __init__(self,L):
        self.edges=L

    def createPaths(self):
        paths={}
        count=0
        for edge in self.edges:
            if edge[:-1] in paths.keys():
                paths[edge[:-1]].append(edge[1:])
            else:
                paths[edge[:-1]]=[edge[1:]]
            count+=1
        if self.edges[-1][1:] in paths.keys():
            paths[self.edges[-1][1:]].append(self.edges[0][:-1])
        else:
            paths[self.edges[-1][1:]]=[self.edges[0][:-1]]
        count+=1
        
        return (paths,count)
    
    def EulerianCycle(self):
        startNode=self.edges[0][:-1]
        
        (allPaths,count)=self.createPaths()
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

def createDeBruijn(kmersList):
    return deBruijnGraph(kmersList)

def rotateList(List,n):
    return List[n:]+List[:n]

def createKmerList(data,k):
    L=[]
    for i in range(len(data)-k+1):
        L.append(data[i:k+i])
    return L

def Genome(path):
    genome=path[0]
    for i in range(1,len(path)):
        genome+=path[i][-1]
    return genome
   
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
    k=int(input())
    L=createKmerList(data,k) 
    stringDifferences=[]
    for i in range(100):
        G=createDeBruijn(L)
        path=G.EulerianCycle()
        finalGenome=Genome(path)
        diff=compareStrings(finalGenome,data)
        stringDifferences.append(diff)
    count=0
    countZeros=0
    for i in stringDifferences:
        count+=i
        if i==0:
            countZeros+=1
    print(count/100)
    print(max(stringDifferences))
    print(countZeros)
