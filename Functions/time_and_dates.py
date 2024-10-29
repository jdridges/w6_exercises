import datetime

#LAB 2 Q 2
today = datetime.datetime.now()
formatted_date = today.strftime("Today is %A, %B %d, %Y")       #why is %d blue???
print(formatted_date)

# output is: Today is Tuesday, October 29, 2024

            #LAB2 Q3
my_birthday = datetime.date(1999, 7, 10)
my_birthday_formatted = my_birthday.strftime("My birthday is %m/%d/%Y")
print(my_birthday_formatted)


            #LAB2 Q4
ninety_d = today + datetime.timedelta(days=90)
ninety_d_formatted = ninety_d.strftime("90 days from today is %B %d, %Y")
print(ninety_d_formatted)


            #LAB2 Q5
dinner_time = datetime.time(17, 30)
dinner_time_formatted = dinner_time.strftime("Lets meet for dinner at %I:%M %p")
print(dinner_time_formatted)