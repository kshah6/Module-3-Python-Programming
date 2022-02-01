# Enter the day of leaving
day = int(input("Which day you will leave: "))
# number of days on leave
travel_day = int(input("How many day you will be gone: "))
# returning day
return_day = (day + travel_day) % 7

print("You will return on", return_day)
