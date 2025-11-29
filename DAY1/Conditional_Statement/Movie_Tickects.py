price=input("Enter the price of the movie ticket: ")
price=float(price)

number_of_tickets=int(input("Enter number"))

catagory=int(input("Enter 1 for Student\n"))

if number_of_tickets>15 and catagory==1:
    total_price=(number_of_tickets*price)*0.75
    print("The discount: ",total_price)
elif number_of_tickets>15 and catagory!=1:
    total_price=(number_of_tickets(price))*0.8
    print("The discount: ",total_price)
elif number_of_tickets<=15 and catagory==1:
    total_price=(number_of_tickets*price)*0.95
    print("The total price: ",total_price)

