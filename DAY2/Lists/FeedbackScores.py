Scores=[1,2,3,4]

even_count=0
odd_count=0

for i in Scores:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers: ",even_count)
print("Odd numbers: ",odd_count)