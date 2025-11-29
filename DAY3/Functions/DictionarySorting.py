products=eval(input("Enter the products: "))
sort_method=input("Enter the sorting type Key or Price: ")
if sort_method=='key':
    sorted_dict=dict(sorted(products.items()))
# SAMPLE INPUT
# {'Laptop': 800, 'Mobile': 400, 'TV': 600,'Headphones': 100}
# SAMPLE INPUT END
elif sort_method=='price':
    sorted_values=sorted(set(products.values()))

    sorted_dict={}

    for i in sorted_values:
        for key in products:
            if products[key]==i:
                sorted_dict[key]=i
else:
    sorted_dict=products
    print("Invalid option.")
print("Sorted Dictionary: ",sorted_dict)