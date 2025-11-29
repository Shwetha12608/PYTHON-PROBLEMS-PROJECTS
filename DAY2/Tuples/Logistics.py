#  (1, 2, 3), (4, 5, 6), (7, 8, 9)

List_of_tuple=input("Enter the list of tuples: ")
List_of_tuple=eval(List_of_tuple)
k=int(input("Enter the column index: "))
product=1
for i in List_of_tuple:
    if k<len(i):
        product=product*i[k]
    else:
        print(f"Invalid {k}")
        break
print(product)