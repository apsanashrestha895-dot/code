from datetime import datetime
birthday_input = input("enter your birthady date(dd:mm:yyyy):")
birthday = datetime.strptime(birthday_input, "%d - %m -%y")
today = datetime.now()
this_year_b = birthday.replace(year = today.year)

if this_year_b < today:
    next_year_b = this_year_b.repalce(year= today.year + 1)
else:
    next_year_b = this_year_b
if this_year_b == today:
    print("happy birthday")    