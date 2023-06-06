# How many seconds are in a year

daysyear = int(input("How many days are in this year?"))
if daysyear == 365:
  sec_y = 60 * 60 * 24 * daysyear
  print("Number of seconds in a year are",sec_y)
else:
  sec_y = (60 * 60 * 24 * daysyear) + 60 * 60 * 24
  print("Number of seconds in a leap year are",sec_y)