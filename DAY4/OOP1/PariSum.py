class PairFinding:
    def __init__(self,Sum,n,Values):
        self.Sum=Sum
        self.n=n
        self.Values=Values
    def findPairs(self):
        n=len(self.Values)
        pairsFound=[]
        for i in range(n):
            for j in range(i+1,n):
                if self.Values[i]+self.Values[j]==self.Sum:
                    pairsFound.append((self.Values[i],self.Values[j]))
        return pairsFound   
    def displayPairs(self):
        pairs=self.findPairs()
        for a,b in pairs:
            print(f"({a}, {b})")    

# MAIN()
Sum=30
n=8
Values=[14,-15,9,16,25,45,12,8]
pairResult=PairFinding(Sum,n,Values)
pairResult.displayPairs()
