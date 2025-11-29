# What is list in python ?

# Collection of items (heterogenous)

# Ordered, Duplicated,Mutable,No sorting required

# Homogenous list
numbers=[10,20,30,40]
# Hetero
mixed=[10,"Name",10.5,False]
# Accessing elements in a list
print(numbers[0])
# Last value
print(numbers[-1])

# Slicing of a list

print(numbers[1:3])

# FUNCTION OF LIST

# 1.Append()

numbers.append(80)
print(numbers)

# 2.Insert()
numbers.insert(2,100)
print("After insertion at position 2: ",numbers)


# 3.Remove()
numbers.remove(100)
print("After removing 100: ",numbers)

# 4.pop()

numbers.pop(2)
print("After removing index 2 from pop(): ",numbers)

# 5.Clear()

numbers.clear()
print("After clearing list: ",numbers)

