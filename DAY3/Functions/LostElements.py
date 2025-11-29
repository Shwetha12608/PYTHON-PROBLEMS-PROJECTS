product_ids=input("Enter product IDs:").split()

unique_set=set()
duplicate_set=set()

for i in product_ids:
    if i in unique_set:
        duplicate_set.add(i)
    else:
        unique_set.add(i)

RemainingValues=unique_set - duplicate_set
print("Values are: ",RemainingValues)
