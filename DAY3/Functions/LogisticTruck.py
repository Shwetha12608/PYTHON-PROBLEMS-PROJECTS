Fuel_efficiency=set(map(float,input("Enter fuel :").split()))
max=-float('inf')
min=float('inf')
for i in Fuel_efficiency:
    if i>max:
        max=i
    if i<min:
        min=i

print("Maximum fuel efficiency is:",max)
print("Minimum fuel efficiency is:",min)

    