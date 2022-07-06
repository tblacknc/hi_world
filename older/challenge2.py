#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

def add_time(start, duration, *dofw):
    
    ampm = ["AM", "PM"]
    daystring = ["Sunday ", "Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday "]
    day = 0
    desthour = 0
    dest12 = 0
    daystr = ""
    
    y = start.split()
    startampm = y[1]
    if startampm == "PM":
        day = .5
        
    time = y[0].split(":")
    minutes = int(time[1])
    hours = int(time[0])
    
    duration = duration.split(":")
    tominutes = int(duration[1])
    tohours = int(duration[0])
        
    destmin = minutes + tominutes
    while destmin >= 60:
        desthour += 1
        destmin -= 60
        
    if destmin >= 0 and destmin <=9:
        destmin = "0" + str(destmin)
    else:
        destmin = str(destmin)    
    
    desthour = desthour + hours + tohours    
    while desthour >= 12:
        dest12 += 1
        desthour -= 12
        
    if desthour == 0:
        desthour = str(12)
    else:
        desthour = str(desthour)
    
     
    while dest12 >= 1:
        day += .5
        dest12 -= 1
    
    if day >= 1 and day < 2:
        daystr = "(next day)"
    elif day >= 2:
        daystr = "(" + str(int(day))+ " days later)"
    
    if day == .5:
        destampm = ampm[1]
    else:
        destampm = ampm[0]
    
    dayofwk = 0    
    if dofw:
        str(dofw)
        if dofw[0].lower() == "sunday": dayofwk = 0
        if dofw[0].lower() == "monday": dayofwk = 1
        if dofw[0].lower() == "tuesday": dayofwk = 2
        if dofw[0].lower() == "wednesday": dayofwk = 3
        if dofw[0].lower() == "thursday": dayofwk = 4
        if dofw[0].lower() == "friday": dayofwk = 5
        if dofw[0].lower() == "saturday": dayofwk = 6

    dayofwk = dayofwk + int(day)
    while dayofwk >= 7:        
        dayofwk -= 7   
    if dofw:    
        dowstr = daystring[dayofwk]
        destampm = " " + destampm + ", "
    else:
        dowstr = " "
        destampm = " " + destampm

    new_time = desthour + ":" + destmin + destampm + dowstr + daystr
    new_time = new_time.strip()

    return new_time
    
print(add_time("3:30 PM", "2:12"))
print("5:42 PM")
print(add_time("11:55 AM", "3:12"))
print("3:07 PM")
print(add_time("9:15 PM", "5:30"))
print("2:45 AM (next day)")
print(add_time("11:40 AM", "0:25"))
print("12:05 PM saturDay")
print(add_time("2:59 AM", "24:00", "saturDay"))
print("2:59 AM, Sunday (next day)")
print(add_time("11:59 PM", "24:05","Wednesday"))
print("12:04 AM, Friday (2 days later)")
print(add_time("8:16 PM", "466:02","tuesday"))
print("6:18 AM, Monday (20 days later)")
