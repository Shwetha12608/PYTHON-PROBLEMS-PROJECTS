class SilverStall:
    def __init__(self,name,detail,owner,cost):
        self.name=name
        self.detail=detail
        self.owner=owner
        self.cost=cost
    def total_cost(self):
        return self.cost
    
class GoldStall(SilverStall):
    def __init__(self,name,detail,owner,cost,tv_set):
        super().__init__(name,detail,owner,cost)
        self.tv_set=tv_set
    def total_cost(self):
        return self.cost+self.tv_set*100
    
class Platinumstall(GoldStall):
        def __init__(self,name,detail,owner,cost,tv_set,projector_set):
             super().__init__(name,detail,owner,cost,tv_set)
             self.projector_set=projector_set

        def total_cost(self):
             return self.cost+self.tv_set*100+self.projector_set*500

# MAIN()

choice =input("Enter the choice 1|2|3: Silver|Gold|Platinum: ")
choice=int(choice)
if choice==1:
     name=input("Enter the name: ").strip()
     detail=input("Enter the detail: ").strip()
     owner=input("Enter the owner name: ").strip()
     cost=int(input("Enter the cost: ").strip())
     stall=SilverStall(name,detail,owner,cost)
     print(stall.total_cost())
if choice==2:
     name=input("Enter the name: ").strip()
     detail=input("Enter the detail: ").strip()
     owner=input("Enter the owner name: ").strip()
     cost=int(input("Enter the cost: ").strip())
     tv_set=int(input("Enter the number of TV sets: ").strip())
     stall=GoldStall(name,detail,owner,cost,tv_set)
     print(stall.total_cost())          

if choice==3:
     name=input("Enter the name: ").strip()
     detail=input("Enter the detail: ").strip()
     owner=input("Enter the owner name: ").strip()
     cost=int(input("Enter the cost: ").strip())
     tv_set=int(input("Enter the number of TV sets: ").strip())
     projector_set=int(input("Enter the number of Projector sets: ").strip())
     stall=Platinumstall(name,detail,owner,cost,tv_set,projector_set)
     print(stall.total_cost())    
else:
        print("Invalid Choice")