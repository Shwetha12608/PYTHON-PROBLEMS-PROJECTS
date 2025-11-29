product_id=input("Enter the product ID: ").split()
print("Enter the k value: ")
k=int(input())
result=[]
for i in product_id:
    if i not in result:
        count=0
        for item in product_id:
            if item==i:
                count=count+1
        if count>k:
                print(f"Product ID {i}:{count} times")
            
        result.append(i)