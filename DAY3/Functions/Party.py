
# TYPES OF FUNCTION

# 1.User-defined function:
# TYPES OF USER-DEFINED FUNCTION
# 1.Parameterized function
# 2.Non-parameterized function
# 3.Returning function
# 4.Non-returning function

# 2.Built-in function
# 3.Anynomous/Lambda function

def classify_party_success(day,attendees):
    valid_days=["SUN","MON","TUE","WED","THU","FRI","SAT"]

    if day not in valid_days or attendees<0:
        return "Invalid Input"    

    # SUCCESS CHECK

    if day in ["FRI","SAT","SUN"]:
        if attendees>=1500:
            return "Party is Successful"
        else:
            return "Unsuccessful"
    else:
        if 700<=attendees<=1000:
            return "Successfull"
        else:
            return "Unsuccessful"


day=input("Enter the day: ").strip().upper()
attendees=int(input("Enter the number of attendees: "))

result=classify_party_success(day,attendees)
print(result)
