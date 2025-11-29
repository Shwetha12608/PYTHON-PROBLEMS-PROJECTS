import datetime as dt
def say_hello(name):
    current_hour=dt.datetime.now().hour

    if current_hour<12:
        greeting="Good Morning"
    elif 12<=current_hour<17:
        greeting="Good Afternoon"
    else:
        greeting="Good Evening"
    
    print(f"{greeting}, {name}!")
