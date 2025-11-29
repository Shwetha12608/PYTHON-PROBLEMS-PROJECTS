Principle_amt=float(input("Enter the amount: "))

rate=0.05 #5%

for i in range(1,11):
    a=Principle_amt*(1+rate)**i
    print(f"{a:.2f}")


    